# coding: UTF-8
#!/usr/bin/env python

import MeCab
import re
import json

def gets_surface(list):
	surface_list = []
	for line in list:
		surface_list.extend([str(line.get("surface"))])
	surface_list = sorted(surface_list)
	return surface_list

def deplicate_delete(list):
	frequency_list = {}
	deplicate_delete_list = set(list)
	for word in deplicate_delete_list:
		frequency_list[word] = 0
	return frequency_list

def gets_frequency(item_list, surface_list):
	for word in surface_list:
		item_list[word] += 1

	frequency_list = {}
	for k, v in sorted(item_list.items(), key=lambda x: -x[1]):
		frequency_list[k] = v

	return frequency_list

try:
	# ローカルJSONファイルの読み込み
	with open('./file/ex30_practice.json', 'r') as f:
		data = json.load(f)
		surface_list         = gets_surface(data)
		emply_frequency_list = deplicate_delete(surface_list)
		frequency_list       = gets_frequency(emply_frequency_list, surface_list)
		print(frequency_list)
except json.JSONDecodeError as e:
	print('JSONDecodeError: ', e)
