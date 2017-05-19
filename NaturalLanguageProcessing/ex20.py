# coding: UTF-8
#!/usr/bin/env python
import codecs
import json

# ファイルを使って開き、透過的なエンコード/デコードする
json_file = codecs.open('./file/jawiki-country.json', 'r', 'utf_8')

if __name__ == "__main__":
	us_list = []
	category_match = open('./file/ex20_practice.txt', 'w')
	for line in json_file:
		file_record = json.loads(line)
		if file_record["title"] == "イギリス":
			us_list.append(file_record)
			category_match.write(str(file_record)+"\n")
	category_match.close()
	# print(us_list)
