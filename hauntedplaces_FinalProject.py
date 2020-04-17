import pandas as pd
import folium
import json
from folium import plugins

# data from here https://data.world/timothyrenner/haunted-places

hauntings = pd.read_csv("haunted_places.csv")

with open('usStates.geojson') as f:
    usStates = json.load(f)

# Initializing map around US
usMap = folium.Map(location=[40.7128, -74.0060], tiles="Stamen Terrain", zoom_start=10)

# Adding shape of USA to the map
folium.GeoJson(usStates).add_to(usMap)

# for each row in the dataset, plot the corresponding latitude and longitude on the map
for i, row in hauntings.iterrows():
    folium.CircleMarker((row.city_latitude, row.city_longitude), radius=1, weight=2, color='blue', fill_color='blue',
                        fill_opacity=.4).add_to(usMap)

# Adding markers for each haunted location
for i in range(0,len(hauntings)):
    folium.Marker([hauntings.iloc[i]['city_latitude'], hauntings.iloc[i]['city_longitude']], popup=hauntings.iloc[i]['location']).add_to(usMap)

# save the map as an html
usMap.save('hauntedUSMap.html')