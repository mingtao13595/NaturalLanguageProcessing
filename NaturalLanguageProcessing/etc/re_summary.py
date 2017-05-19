# coding: UTF-8
#!/usr/bin/env python
import codecs
import json
import re

# ファイルを使って開き、透過的なエンコード/デコードする
json_file = codecs.open('./file/jawiki-country.json', 'r', 'utf_8')
# 正規表現を書く
# repatter  = re.compile('.+section=1.+')
# repatter  = re.compile('.+section=.+')
# repatter  = re.compile('^=')
# repatter  = re.compile('.+=[0-9].+')

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

def delete_japanese_char(str):
	# import re をしないと使えない
	flow_str = re.sub(r'[一-龠]+|[ぁ-ん]+|[ァ-ヴ]+', '', str)
	flow_str = re.sub('「', '', flow_str)
	flow_str = re.sub('」', '', flow_str)
	flow_str = re.sub('、', '', flow_str)
	flow_str = re.sub('。', '', flow_str)
	flow_str = re.sub('ー', '', flow_str)
	flow_str = re.sub('・', '', flow_str)
	flow_str = re.sub('（', '', flow_str)
	flow_str = re.sub('）', '', flow_str)
	flow_str = re.sub('()', '', flow_str)
	flow_str = re.sub(r'\'{1,}', '', flow_str)
	return flow_str

def delete_dot_after_number(str):
	flow_str = re.sub(r'\.[0-9]{1,2}', '', str)
	return flow_str

def delete_meta_char(str):
	# import re をしないと使えない
	flow_str = re.sub(r'\[{1,}', '', str)
	flow_str = re.sub(r'\]{1,}', '', flow_str)
	# flow_str = re.sub(r'\|', '', flow_str)
	return flow_str

if __name__ == "__main__":
	articleList = []
	us_list = search_list("イギリス")
	for line in us_list:
		fileLineList = line['text'][:-1].split('\n')
		for element in fileLineList:
			element_small_num = delete_dot_after_number(element)

			if element_small_num.find('.') != -1:
				section_word = element_small_num
				# section_word = delete_japanese_char(element_small_num)
				# section_word = delete_meta_char(section_word)
				# section_word = delete_dot_after_number(section_word)
				extension = re.findall(r'\.[A-z]{1,}', section_word)
				print(extension)
				print("------------------------")
				# articleList.append(element)

	# category_match = open('./file/ex24_practice.txt', 'w')
	# section = {}
	# for line in articleList:
	# 	section_level = line.count('=')
	# 	section_level_num = section_level/2 - 1.0
	# 	section_word = re.sub('=', '', line)
	# 	section_word = re.sub(' ', '', section_word)
	# 	category_match.write(section_word + ":" + str(section_level_num))
	# 	section[section_word] = section_level_num
	# print(section)
	# category_match.close()
