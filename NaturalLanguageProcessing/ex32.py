# coding: UTF-8
#!/usr/bin/env python

import MeCab
import re
import json

def gets_verb(list):
	verbList = []
	for line in list:
		if line.get("base") == "動詞":
			verbList.append(line["pos5"])
			# print(line)
	return verbList

try:
	# ローカルJSONファイルの読み込み
	with open('./file/ex30_practice.json', 'r') as f:
		data = json.load(f)
		verbList = gets_verb(data)
		print(verbList)
except json.JSONDecodeError as e:
	print('JSONDecodeError: ', e)
