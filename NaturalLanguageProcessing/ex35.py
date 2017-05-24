# coding: UTF-8
#!/usr/bin/env python

import MeCab
import re
import json

def gets_articulated(list):
	count = 0
	articulated_list = []
	temp_str = '';
	for line in list:
		if temp_str == line.get("surface"):
			articulated_list.append(line)
		count += 1
		temp_str = line.get("surface")
	return articulated_list

try:
	# ローカルJSONファイルの読み込み
	with open('./file/ex30_practice.json', 'r') as f:
		data = json.load(f)
		# print(data)
		articulated_list = gets_articulated(data)
		print(articulated_list)
except json.JSONDecodeError as e:
	print('JSONDecodeError: ', e)
