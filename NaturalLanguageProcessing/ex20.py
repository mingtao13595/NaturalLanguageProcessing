# coding: UTF-8
#!/usr/bin/env python
import codecs
import json

# ファイルを使って開き、透過的なエンコード/デコードする
json_file = codecs.open('./file/jawiki-country.json', 'r', 'utf_8')

if __name__ == "__main__":
	for line in json_file:
		file_record = json.loads(line)
		if file_record["title"] == "イギリス":
			# print(file_record)
			with codecs.open('UK.txt', 'w', 'utf_8') as file:
				file.write(file_record["text"])
