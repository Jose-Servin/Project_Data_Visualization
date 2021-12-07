import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# open json and dump data into variable
file_path = ('Chapter_16/stations.json')
with open(file_path) as f:
    data_file = json.load(f)

readable_station_file = ('Chapter_16/readable_stations.json')
with open(readable_station_file, 'w') as new_file:
    json.dump(data_file, new_file, indent=4)

station_dictionaries = data_file['features']
print(len(station_dictionaries))


# Extracting description, longitude and latitude 
descriptions, lons, lats = [], [], []

for dictionary in station_dictionaries:
    lon = dictionary['geometry']['coordinates'][0] # we reference dictionary because that's what the data is stored in
    lat = dictionary['geometry']['coordinates'][1]
    desc = dictionary['properties']['description']

    lons.append(lon)
    lats.append(lat)
    descriptions.append(desc)


print(lons[:3])
print(lats[:3])
print(descriptions[:3])

# Map out the metro station data 
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title="Metro Stations in Washington DC")
fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='Washington DC Metro Stations.html')