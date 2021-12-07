import json

file_path = ('Chapter_16/eq_data_1_day_m1.json')
with open(file_path) as json_file:
    data = json.load(json_file)

readable_file = ('Chapter_16/readable_file.json')
with open (readable_file, 'w') as new_file:
    json.dump(data, new_file, indent=4)

earthquake_dictionaries = data['features'] # reading for original variable containing json data 
print(len(earthquake_dictionaries))

# Extracting magnitude data 
