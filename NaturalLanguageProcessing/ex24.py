#!/usr/bin/env python
# coding: UTF-8
import codecs
import json
import re

# ファイルを使って開き、透過的なエンコード/デコードする
json_file = codecs.open('./file/jawiki-country.json', 'r', 'utf_8')

def search_list(str):
	result_list = []
	for line in json_file:
		file_record = json.loads(line)
		if file_record["title"] == str:
			result_list.append(file_record)
	return result_list

if __name__ == "__main__":
	extractionMediaFileList = []
	us_list = search_list("イギリス")
	for line in us_list:
		fileLineList = line['text'][:-1].split('\n')
		for element in fileLineList:
			hit_file = re.findall("(File|ファイル):(?P<Filename>.+\..{3})\|",element)
			extractionMediaFileList.extend(hit_file)
	# 重複削除
	flowExtractionMediaFileList= set(extractionMediaFileList)

	MediaFileList = []
	for line in flowExtractionMediaFileList:
		MediaFileList.append(line[1])

	print(MediaFileList)
