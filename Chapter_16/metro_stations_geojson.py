import json

# open json and dump data into variable
file_path = ('Chapter_16/stations.json')
with open(file_path) as f:
    data = json.load(f)

readable_station_file = ('Chapter_16/readable_stations.json')
with open(readable_station_file, 'w') as new_file:
    json.dump(data, new_file, indent=4)

station_dictionaries = data['features']
print(len(station_dictionaries))


# Extracting description, longitude and latitude 