# coding: UTF-8
import re

input_value = input()
# 標準入力の値処理
result = "";
repatter_int = re.compile('\d')

if repatter_int.match(input_value):
	result = int(input_value)
else:
	result = "整数値を入力してください"

if result != "整数値を入力してください":
	f   = open('./file/hightemp.txt', 'r')
	fileList   = []
	for line in f:
		lineList = line[:-1]
		fileList.append(lineList)
	f.close()

	split = round(len(fileList)/result)

	for i in range(len(fileList)):
		if float(i) % float(split) == 0.0:
			print("-----------------------------")
		print(fileList[len(fileList)-1-i])

print(result);
