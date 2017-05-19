# coding: UTF-8
#!/usr/bin/env python
import codecs
import json
import re

# ファイルを使って開き、透過的なエンコード/デコードする
json_file = codecs.open('./file/jawiki-country.json', 'r', 'utf_8')
# 正規表現を書く
repatter  = re.compile('Category:.+\]')

if __name__ == "__main__":
	articleList = []
	for line in json_file:
		file_record  = json.loads(line)
		fileLineList = line[:-1].split('\\n')
		articleList.append(fileLineList)

	category_match = open('./file/ex22_practice.txt', 'w')

	for line in articleList:
		for raw in line:
			category_row = repatter.findall(raw)
			if len(category_row) != 0:
				category_word = category_row[0]
				# 扶養文字列削除
				category_word = re.sub(r']].+', '', category_word)
				category_word = re.sub(']]'   , '', category_word)
				category_word = re.sub(r'\|.+', '', category_word)
				category_match.write(category_word + "\n")
				print(category_word)
	category_match.close()
