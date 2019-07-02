from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from lxml import etree
import random
from os import path, makedirs


def config():
    return {
        "debug": False,
        "cache": "downloads"
    }


def load_files(ressource, debug=True, filter_=None):
    
    if not path.exists(config()["cache"]):
        makedirs(config()["cache"])
        
    if not path.exists(path.join(config()["cache"], ressource["identifier"])):
        
        print("downloading {}".format(ressource["url"]))
        with open(path.join(config()["cache"], ressource["identifier"]), "wb") as fout:
            stream = urlopen(ressource["url"]).read()
            fout.write(stream)
            
    
    zipped_ressource = ZipFile(path.join(config()["cache"], ressource["identifier"]))

    namelist = zipped_ressource.namelist()
    
    if filter_ is not None:
        namelist = [fn for fn in namelist if filter_ not in fn]
    
    if debug:
        namelist = random.sample(namelist, 50)

    for name in namelist:
        yield zipped_ressource.open(name).read()
    


def dta_loader():

    ressource = {
        "url" : "http://media.dwds.de/dta/download/dta_kernkorpus_belletristik_2018-10-17.zip",
        "identifier": "dta_kernkorpus_belletristik_2018-10-17.zip"
    }
    
    for file_bytes in load_files(ressource, debug=config()["debug"]):
        try:
            yield etree.XML(file_bytes)
        except etree.XMLSyntaxError:
            pass

            
def wilhelmus_loader():

    ressource = {
        "url" : "https://github.com/fbkarsdorp/meertens-song-collection/archive/DH2019.zip",
        "identifier": "DH2019.zip"
    }
    
    for file_bytes in load_files(ressource, debug=config()["debug"], filter_="/test/"):
        try:
            yield etree.XML(file_bytes)
        except etree.XMLSyntaxError:
            pass

def bi_loader():
    
    ressource = {
        "url": "https://www.berliner-intellektuelle.eu/berliner-intellektuelle-manuscripts.zip",
        "identifier": "berliner-intellektuelle-manuscripts.zip"
    }

    for file_bytes in load_files(ressource, debug=config()["debug"]):
        try:
            yield etree.XML(file_bytes)
        except etree.XMLSyntaxError:
            pass


def extract_text_versions_from_etree(tree):
    '''traverse an etree recursively and extract plain text for initial
       and final version of the text. This is an oversimplified implementation
       because it does not consider <note> and <addSpan> and <delSpan>.
    '''
    doc = []
    in_init_version = []
    in_final_version = []

    def __in_final_version(crumbs):
        return "del" not in [x.tag[-3:] for x in crumbs if type(x.tag)==str]

    def __in_initial_version(crumbs):
        return "add" not in [x.tag[-3:] for x in crumbs if type(x.tag)==str]

    def __traverse_and_parse(el, doc, in_init_version, in_final_version, parents=list()):
        
        parents += [el]

        if el.text is not None:
            doc += [el.text]
            in_init_version += [__in_initial_version(parents)] * len(el.text)
            in_final_version += [__in_final_version(parents)] * len(el.text)

        for gen in el:
            __traverse_and_parse(gen, doc, in_init_version, in_final_version, parents)

        del parents[parents.index(el)]

        if el.tail is not None:
            doc += [el.tail]
            in_init_version += [__in_initial_version(parents)] * len(el.tail)
            in_final_version += [__in_final_version(parents)] * len(el.tail)

    __traverse_and_parse(tree, doc, in_init_version, in_final_version)

    return "".join(doc), in_init_version, in_final_version