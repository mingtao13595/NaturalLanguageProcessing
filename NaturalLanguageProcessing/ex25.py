#!/usr/bin/env python
# coding: UTF-8
import codecs
import json
import re

# ファイルを使って開き、透過的なエンコード/デコードする
json_file = codecs.open('./file/jawiki-country.json', 'r', 'utf_8')
repatter = re.compile('\{')


def search_list(str):
	result_list = []
	for line in json_file:
		file_record = json.loads(line)
		if file_record["title"] == str:
			result_list.append(file_record)
			# result_list.extend(file_record)
	return result_list

# ディクショナリー構造をツリー構造化して出すメソッド
def dictionary_tree(dictionary):
	tree_box = []
	for key, value in dictionary.items():
		tree_box.append(key)
		if isinstance(value, dict) == True:
			dictionary_tree(value)
		else:
			print(tree_box)
		tree_box.pop()

def converte_dictionary(list):
	result_dictionary = {}

	for line in list:
		for char in line:
			

		new_line_list = list[:-1].split('{')

		result_dictionary.append(new_line_list)

if __name__ == "__main__":
	extractionMediaFileList = []
	us_list = search_list("イギリス")

	temp_list = []
	for line in us_list:
		new_line_list = line['text'][:-1].split('{')
		# for line in new_line_list:
		# 	kuten_list = line['text'][:-1].split('。')
		# 	temp_list.extend(kuten_list)
		temp_list.extend(new_line_list)
	# print(temp_list[100])

	print(len(temp_list))
