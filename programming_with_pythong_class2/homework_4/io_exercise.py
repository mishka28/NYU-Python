#!/usr/bin/env python3

import json
import csv
import yaml
import pprint

pp = pprint.PrettyPrinter(indent=4)

file_name_json = 'input.json'
file_name_yaml = 'input.yaml'
file_name_csv = 'input.csv'
output_name_json = 'output.json'
output_name_yaml = 'output.yaml'
output_name_csv = 'output.csv'


data = dict()

with open(file_name_csv, 'r') as csvfile:
    d_reader = csv.DictReader(csvfile)
    dict_list = []

    # headers = d_reader.fieldnames
    # print(headers)

    for x in d_reader:
        dict_list.append(x)

with open(file_name_json, 'w') as f_json:
    json.dump(dict_list,f_json,sort_keys=True,indent=4, separators=(',', ': '))

with open(file_name_yaml, 'w') as f_yaml:
    yaml.dump(dict_list,f_yaml,default_flow_style=False,explicit_start=True)

with open(file_name_yaml, 'r') as f_yaml:
    yaml_str = yaml.load(f_yaml)
with open(file_name_json, 'r') as f_json:
    json_str = json.load(f_json)

super_dict = {}
super_dict.update({'csv':dict_list, 'json':json_str, 'yaml':yaml_str})

with open(output_name_csv, 'w') as csvfile:
    d_writer = csv.writer(csvfile)
    for key, value in super_dict.items():
        d_writer.writerow([key, value])
with open(output_name_json, 'w') as f_json:
    json.dump(super_dict,f_json,sort_keys=True,indent=4, separators=(',', ': '))
with open(output_name_yaml, 'w') as f_yaml:
    yaml.dump(super_dict,f_yaml,default_flow_style=False,explicit_start=True)

'''
reader = csv.DictReader(file_name_csv,)

with open(file_name_json, 'w') as f:
    data['new_key'] = [1,2,3]
    json.dump(data,f)
'''
# with open(output_name_csv, 'w') as csvfile:

#     fieldnames = []
#     for key in super_dict:
#         fieldnames.append(key)
#     print(fieldnames)
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel')
#     writer.writeheader()
#     writer.writerows(str(super_dict.values()))
#         # for row in value:
#         #     writer.writerow(row)

