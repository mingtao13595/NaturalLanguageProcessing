# coding: utf-8
import codecs
import json
import re

def extract_UK():
	json_file = codecs.open('./file/jawiki-country.json', 'r', 'utf_8')
	for line in json_file:
		data_json = json.loads(line)
		if data_json['title'] == 'イギリス':
			return data_json['text']
	raise ValueError('イギリスの記事が見つからない')

# 基礎情報テンプレートの抽出条件のコンパイル
pattern = re.compile(r'''^\{\{基礎情報.*?$(.*?)^\}\}$''', re.MULTILINE + re.VERBOSE + re.DOTALL)
# 基礎情報テンプレートの抽出
contents = pattern.findall(extract_UK())
# 抽出結果からのフィールド名と値の抽出条件コンパイル
pattern = re.compile(r'''^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)| (?=\n$))''', re.MULTILINE + re.VERBOSE + re.DOTALL)
# フィールド名と値の抽出
fields = pattern.findall(contents[0])
#
pattern_delete_markup = re.compile(r'''\<(.+?)\>''', re.MULTILINE + re.VERBOSE + re.DOTALL)

fields_delete_markup = {}
for line in fields:
	word_delete_markup = re.sub(r'''\'{1,4}''', '', line[1])
	word_delete_markup = re.sub(r'''\[http:\/\/(.+?)\]''', '', word_delete_markup)
	word_delete_markup = re.sub(r'''\[\[|\]\]''', '', word_delete_markup)
	word_delete_markup = re.sub(r'''\<ref\>|\<\/ref\>''', '', word_delete_markup)
	word_delete_markup = re.sub(r'''\<ref (.+?)\>''', '', word_delete_markup)
	word_delete_markup = re.sub(r'''\<br\/\>|\<br \/\>''', '', word_delete_markup)
	word_delete_markup = re.sub(r'''\(&(.+?)\)''', '', word_delete_markup)
	word_delete_markup = re.sub(r'''\*''', '', word_delete_markup)

	word_delete_markup = re.sub(r'''\{\{|\}\}''', '', word_delete_markup)

	fields_delete_markup[line[0]] = word_delete_markup
	# print(line[0]+":"+word_delete_markup)

print(fields_delete_markup)
