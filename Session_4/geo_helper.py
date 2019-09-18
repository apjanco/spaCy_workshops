import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
import geopandas as gpd
import json
import urllib
import iso3166

def get_iso_a3_of_str(LOC):
    url_str = "https://nominatim.openstreetmap.org/search/{}?format=json&addressdetails=1".format(urllib.parse.quote(LOC))
    request = urllib.request.urlopen(url_str)
    data = request.read()
    
    encoding = request.info().get_content_charset('utf-8')
    JSON_object = json.loads(data.decode(encoding))
    df = pd.DataFrame(JSON_object)
    try:
        country_code = df.sort_values("importance")[::-1].iloc[0].address["country_code"]
        iso_alpha3 = iso3166.countries.get(
            country_code
        ).alpha3

        # print(LOC, ", ", country_code, ", ", iso_alpha3)
        return iso_alpha3
    except KeyError:
        return None

def plot_countries(cnts):

    cmap = cm.get_cmap('Blues')


    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    
    # add missing iso_a3 codes
    world.loc[world.name=="France", "iso_a3"] = "FRA"
    world.loc[world.name=="Norway", "iso_a3"] = "NOR"
    world.loc[world.name=="Somaliland", "iso_a3"] = "SOM"
    world.loc[world.name=="Kosovo", "iso_a3"] = "XKX"


    world["references"] = world.T.apply(lambda x: 0 if x.iso_a3 not in cnts else cnts[x.iso_a3])
    world = world[(world.name != "Antarctica") & (world.name != "Fr. S. Antarctic Lands")]
    world = world.to_crs({'init': 'epsg:3395'})
    world.plot(
        column="references",
        figsize=(30,30),
        cmap=cmap,
    )

