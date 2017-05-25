# coding: UTF-8
#!/usr/bin/env python

import MeCab
import re
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

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

def top_ten(list):
	top_ten_list = {}
	for k, v in list.items():
		if len(top_ten_list) == 10:
			return top_ten_list
		if (k != '*')&(k != '。')&(k != '、'):
			top_ten_list[k] = v

try:
	# ローカルJSONファイルの読み込み
	with open('./file/ex30_practice.json', 'r') as f:
		data = json.load(f)
		surface_list         = gets_surface(data)
		emply_frequency_list = deplicate_delete(surface_list)
		frequency_list       = gets_frequency(emply_frequency_list, surface_list)
		top_ten_list         = top_ten(frequency_list)

		words  = []
		counts = []
		for k,v in top_ten_list.items():
			words.extend(k)
			counts.extend([v])

		# グラフで使うフォント情報(デフォルトのままでは日本語が表示できない)
		fp = FontProperties(
			fname='/usr/share/fonts/migu-1p-20150712/migu-1p-regular.ttf'
		)

		size = len(top_ten_list)

		plt.bar(
			range(0, size),
			counts,
			align='center'
		)

		plt.xticks(
			range(0, size),
			words,
			fontproperties=fp
		)

		plt.xlim(
			xmin=-1, xmax=size
		)

		plt.title(
			'37. 頻度上位10語',
			fontproperties=fp
		)
		plt.xlabel(
			'出現頻度が高い10語',
			fontproperties=fp
		)
		plt.ylabel(
			'出現頻度',
			fontproperties=fp
		)

		plt.grid(axis='y')

		plt.show()

except json.JSONDecodeError as e:
	print('JSONDecodeError: ', e)
