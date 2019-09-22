import pandas as pd
from os import path, makedirs
import requests

def get_urllist():
    return pd.DataFrame([
        {"play_id": "jn", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-jn.xml"},
        {"play_id": "r2", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-r2.xml"},
        {"play_id": "1h4", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-1h4.xml"},
        {"play_id": "2h4", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-2h4.xml"},
        {"play_id": "h5", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-h5.xml"},
        {"play_id": "1h6", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-1h6.xml"},
        {"play_id": "2h6", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-2h6.xml"},
        {"play_id": "3h6", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-3h6.xml"},
        {"play_id": "r3", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-r3.xml"},
        {"play_id": "h8", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-h8.xml"},
        {"play_id": "rom", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-rom.xml"},
        {"play_id": "mnd", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-mnd.xml"},
        {"play_id": "jc", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-jc.xml"},
        {"play_id": "tn", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-tn.xml"},
        {"play_id": "tem", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-tem.xml"},
        {"play_id": "ham", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-ham.xml"},
        {"play_id": "mv", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-mv.xml"},
        {"play_id": "ayl", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-ayl.xml"},
        {"play_id": "shr", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-shr.xml"},
        {"play_id": "ado", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-ado.xml"},
        {"play_id": "lll", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-lll.xml"},
        {"play_id": "cor", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-cor.xml"},
        {"play_id": "err", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-err.xml"},
        {"play_id": "tgv", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-tgv.xml"},
        {"play_id": "wiv", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-wiv.xml"},
        {"play_id": "wt", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-wt.xml"},
        {"play_id": "tit", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-tit.xml"},
        {"play_id": "ant", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-ant.xml"},
        {"play_id": "mm", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-mm.xml"},
        {"play_id": "tim", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-tim.xml"},
        {"play_id": "lr", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-lr.xml"},
        {"play_id": "tro", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-tro.xml"},
        {"play_id": "aww", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-aww.xml"},
        {"play_id": "oth", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-oth.xml"},
        {"play_id": "mac", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-mac.xml"},
        {"play_id": "cym", "url": "http://firstfolio.bodleian.ox.ac.uk/download/xml/F-cym.xml"},
    ])

def download(url, location, filename):

    if not path.exists(location):
        makedirs(location)
    r = requests.get(url)
    with open(path.join(location, filename+ ".xml"), "wb") as fout:
        fout.write(r.content)


def get_file_descriptors(cache_dir="downloads"):

    index = get_urllist()

    for _,row in index.iterrows():
        download(row.url, cache_dir, row.play_id)
        yield path.join(cache_dir, row.play_id + ".xml")