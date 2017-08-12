#!/usr/bin/env python3

import json
import csv

file_name_json = "input.json"
file_name_csv = "input.csv"

data = dict()

with open(file_name_csv, "r") as csvfile:
	d_reader = csv.DictReader(csvfile)

	headers = d_reader.fieldnames
	print(headers)

with open(file_name_json, "w") as f:
	data["new_key"] = [1,2,3]
	json.dump(data, f)
