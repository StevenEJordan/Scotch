import datetime

start = datetime.datetime.now()
print('Script started:')
print(start)

import pandas as pd
import folium
from folium.plugins import MarkerCluster, MeasureControl, HeatMap, HeatMapWithTime




#Create Map
m = folium.Map(location=[57, -4], zoom_start=7, tiles='cartodbpositron')
folium.TileLayer('stamenterrain').add_to(m)

scotch = pd.read_csv("whisky.csv")

Locations = scotch[['Lat', 'Lon']]
Location_List = Locations.values.tolist()

dist = folium.FeatureGroup(name='Distilleries')
for point in range(0, len(Location_List)):
    folium.Marker(Location_List[point],  
                  icon=folium.Icon(color='blue', icon='building')
                  ).add_to(dist)

dist.add_to(m)

folium.LayerControl(collapsed=False).add_to(m)
m.add_child(MeasureControl())

m.save('scotch.html')

print('Map Created')

end = datetime.datetime.now()
print('Script completed:')
print(end)

print('Total time elapsed:')
print(end - start)