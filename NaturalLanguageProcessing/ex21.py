# coding: UTF-8
#!/usr/bin/env python
import codecs
import json
import re

# ファイルを使って開き、透過的なエンコード/デコードする
json_file = codecs.open('./file/jawiki-country.json', 'r', 'utf_8')
repatter_int = re.compile('.+Category.+')

if __name__ == "__main__":
	articleList = []
	for line in json_file:
		file_record  = json.loads(line)
		fileLineList = line[:-1].split('\\n')
		articleList.append(fileLineList)

	category_match = open('./file/ex21_practice.txt', 'w')
	for line in articleList:
		for raw in line:
			category_row = repatter_int.findall(raw)
			if len(category_row) != 0:
				category_match.write(str(category_row)+"\n")
				# print(category_row)
	category_match.close()
