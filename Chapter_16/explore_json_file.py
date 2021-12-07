import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

file_path = ('Chapter_16/eq_data_1_day_m1.json')
with open(file_path) as json_file:
    data = json.load(json_file)

readable_file = ('Chapter_16/readable_file.json')
with open (readable_file, 'w') as new_file:
    json.dump(data, new_file, indent=4)

earthquake_dictionaries = data['features'] # reading from original variable containing json data 
print(len(earthquake_dictionaries))

# Extracting magnitude data, longitude and latitude (x and y)
mags, lons, lats  = [], [], []
for dictionary in earthquake_dictionaries:
    mag = dictionary['properties']['mag']
    mags.append(mag)

    lon = dictionary['geometry']['coordinates'][0]
    lons.append(lon)

    lat = dictionary['geometry']['coordinates'][1]
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])

# Map the earthquake data 
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename = 'global_earthquakes.html')