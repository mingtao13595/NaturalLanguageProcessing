# coding: UTF-8
#!/usr/bin/env python

import MeCab
import re
import json

def gets_join_num(list):
	count = 0
	countList = []
	for line in list:
		if (line.get("surface") == "の") & (count > 0):
			countList.extend([count])
		count += 1
	return countList

def gets_join(list, numList):
	noun_phrase_list = []
	for i in numList:
		noun_phrase_list.extend([str(list[i-1]["surface"])+str(list[i]["surface"])+str(list[i+1]["surface"])])
	return noun_phrase_list

try:
	# ローカルJSONファイルの読み込み
	with open('./file/ex30_practice.json', 'r') as f:
		data = json.load(f)
		# print(data)
		gets_join_num    = gets_join_num(data)
		noun_phrase_list = gets_join(data, gets_join_num)
		# print(noun_phrase_list)
except json.JSONDecodeError as e:
	print('JSONDecodeError: ', e)
