# coding: UTF-8
#!/usr/bin/env python
import codecs
import json
import re

# ファイルを使って開き、透過的なエンコード/デコードする
json_file = codecs.open('./file/jawiki-country.json', 'r', 'utf_8')
repatter = re.compile('.+Category.+')

def search_list(str):
	result_list = []
	for line in json_file:
		file_record = json.loads(line)
		if file_record["title"] == str:
			result_list.append(file_record)
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

if __name__ == "__main__":
	articleList = []
	us_list = search_list("イギリス")
	for line in us_list:
		# dictionary_tree(line)
		fileLineList = line['text'][:-1].split('\n')
		articleList.append(fileLineList)

	category_match = open('./file/ex21_practice.txt', 'w')
	for line in articleList:
		for raw in line:
			category_row = repatter.findall(raw)
			if len(category_row) != 0:
				category_match.write(str(category_row)+"\n")
				print(category_row)
	category_match.close()
