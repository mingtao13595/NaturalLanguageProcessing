# coding: UTF-8
#!/usr/bin/env python

import MeCab
import re
# import copy
# import optparse
import codecs
import json

# f = open('./file/neko_morphologicalAnalysis.txt', 'r')
# f = open('./file/ex30_practice.txt', 'r')
# ファイルを使って開き、透過的なエンコード/デコードする
json_file = codecs.open('./file/ex30_practice.json', 'r', 'utf_8')

if __name__ == "__main__":
	us_list = []
	# print(type(json_file))
	for line in json_file:
		# print(line)
		file_record = json.loads(line)
		# us_list.append(file_record)
	# print(us_list)

# parser = optparse.OptionParser()
#
# for line in f:
# 	options = parser.parse_args()
#
# 	print(type(line))
# 	print(line)
# 	# dict_line = dict(line)
# 	# print(dict_line)
# 	# print(type(dict_line))
# 	break
