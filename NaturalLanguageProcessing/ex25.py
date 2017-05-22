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
# 辞書にセット
result    = {}
keys_test = []
for field in fields:
	result[field[0]] = field[1]
	keys_test.append(field[0])
# 確認のため表示（確認しやすいようにkeys_testを使ってフィールド名の出現順にソート）
for item in sorted(result.items(),
		key=lambda field: keys_test.index(field[0])):
	print(item)
