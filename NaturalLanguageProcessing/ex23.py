# coding: UTF-8
#!/usr/bin/env python
import codecs
import json
import re

# ファイルを使って開き、透過的なエンコード/デコードする
json_file = codecs.open('./file/jawiki-country.json', 'r', 'utf_8')

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

def search_list(str):
	result_list = []
	for line in json_file:
		file_record = json.loads(line)
		if file_record["title"] == str:
			result_list.append(file_record)
	return result_list


if __name__ == "__main__":
	articleList = []
	us_list = search_list("イギリス")
	for line in us_list:
		fileLineList = line['text'][:-1].split('\n')
		for element in fileLineList:
			if re.match(r'^=', element):
				articleList.append(element)

	category_match = open('./file/ex23_practice.txt', 'w')
	section = {}
	for line in articleList:
		section_level = line.count('=')
		section_level_num = section_level/2 - 1.0
		section_word = re.sub('=', '', line)
		section_word = re.sub(' ', '', section_word)
		category_match.write(section_word + ":" + str(section_level_num))
		section[section_word] = section_level_num
	print(section)
	category_match.close()
