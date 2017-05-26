# coding: UTF-8
#!/usr/bin/env python

import re
def morphologicalAnalysis(text):
	text_line = re.sub(r"\.|\;|\:|\?|\!", ' ', text)
	# 結果を行単位で分割
	rowList = text_line.split(' ')
	return rowList

f = open('./file/nlp.txt', 'r')
result_line = []
for line in f:
	result_line.extend(morphologicalAnalysis(line))

for line in result_line:
	print(line)
