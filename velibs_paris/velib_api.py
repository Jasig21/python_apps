import json
import copy
import geopandas as gpd
import folium
import matplotlib.pyplot as plt
from folium import plugins 
from folium.plugins import MarkerCluster

url_local = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"
url_nb = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json"

#Récupération de la donnée à partir des liens de l'API Vélib'
localisation = requests.get(url_local) #Données relatives à la localisation des stations Vélib'
nombre = requests.get(url_nb) #Données relatives au nombre de vélos et de bornettes disponibles par station

#Chargement de la donnée sous format json
data_local = json.loads(localisation.content)
data_nb = json.loads(nombre.content)

#Normalisation de la donnée sous forme de data-frame afin de pouvoir les manipuler avec géopandas
#Le geoJson relatif aux locaisations n'a pas besoin de plus de traitements que ça, c'est une structure assez simple
df_local = pd.json_normalize(data_local['data'], record_path =['stations'])

#Le geoJSON du nombre de velib' a quant à lui une structure plus complexe puisqu'il contient un tableau dans un tableau
stations = copy.deepcopy(data_nb['data']['stations'])
for station in stations:
    bikes_types = station.pop("num_bikes_available_types")
    for bike_type in bikes_types:
        bikes_dict = {k:v for k,v in bike_type.items()}
        station.update(bikes_dict)
        
df_nb = pd.json_normalize(stations)

#Jointure des deux tableaux sur la base du champs ID 
df_final = pd.merge(df_local, df_nb, how='inner', left_on='station_id', right_on='station_id')

#Nous remarquons que deux champs sont doublés après la jointure, on les retire
df_final_cleen = df_final.drop(columns=["stationCode_y", "num_bikes_available", "num_docks_available"])



#CARTOGRAPHIE 

myMap = folium.Map(location=[48.865983, 2.275725], zoom_start=10, tiles='CartoDB positron')

# create a marker cluster called "Public toilet cluster"
marker_cluster = folium.plugins.MarkerCluster("Stations Velib").add_to(myMap)
 
#add a marker for each toilet, add it to the cluster, not the map
for each in df_final_cleen.iterrows():
    popup = 'Add <b>test</b>'
    folium.Marker(location=[row["lat"], row["lon"]], popup=popup).add_to(marker_cluster)

myMap