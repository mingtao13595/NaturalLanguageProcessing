# coding: UTF-8
#!/usr/bin/env python

import MeCab
import re
import json

try:
	# ローカルJSONファイルの読み込み
	with open('./file/ex30_practice.json', 'r') as f:
	# with open('./file/test.json', 'r') as f:
		data = json.load(f)
		print(data)
except json.JSONDecodeError as e:
	print('JSONDecodeError: ', e)
