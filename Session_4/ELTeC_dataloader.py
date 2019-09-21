from os import path, makedirs, getcwd, listdir
import subprocess

def config():
    return {
        "cache": "downloads"
    }

    
def download(ressource):
    
    out_path = path.join(getcwd(), config()["cache"], ressource["identifier"])
    if not path.exists(out_path):
        makedirs(out_path)
    
    if len(listdir(out_path)) < 2:
        print("downloading {}".format(ressource["url"]))
        
        p = subprocess.Popen("svn checkout {}".format(ressource["url"]), cwd=out_path, shell=True)
        p.communicate()
        p = subprocess.Popen("mv level1/* .", cwd=out_path, shell=True)
        p.communicate()
        p = subprocess.Popen("rm -rf level1", cwd=out_path, shell=True)
        p.communicate()
    

def get_file_descriptors():

    ressource = {
        "url" : "https://github.com/COST-ELTeC/ELTeC-fra/trunk/level1",
        "identifier": "ELTeC-fra"
    }
    
    download(ressource)
        
    
    for file_desc in listdir(path.join(config()["cache"], ressource["identifier"])):
        yield path.join(config()["cache"], ressource["identifier"], file_desc)
