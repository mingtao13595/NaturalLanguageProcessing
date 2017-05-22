#!/usr/bin/env python
# coding: UTF-8
import re
import copy

# appendは参照私ということに注意する
def converte_dictionary(list):
	result_dictionary = {}
	for line in list:
		str_list  = []
		char_list = []
		for char in line:
			if re.match('{' , char):
				# リストの値をコピー
				input_char_list = copy.deepcopy(char_list)
				str_list.append(input_char_list)
				del char_list[:]
			elif re.match('}' , char):
				# リストの値をコピー
				input_char_list = copy.deepcopy(char_list)
				str_list.append(input_char_list)
				str_list.append(["end"])
				del char_list[:]
			else:
				char_list.extend(char)

		# print(str_list)
		num_list = []
		num = 0;
		for line in str_list:
			if line == []:
				num += 1
				num_list.append(num)
			elif line == ["end"]:
				num -= 1
				num_list.append(num)
			else:
				num_list.append(num)
		print(num_list)
		num_list_plus = []
		for num in num_list:


	# print(len(str_list))
	# print(len(num_list))
	#
	result_list = []
	count = 0
	temp_num = 0
	for line in num_list:


		temp_num = line
		count += 0

		# for line in str_list:
		# 	print(line)

sample = ["{{AAA},aaaaaaa}{{ｐｐｐｐｐｐ} {ｐｐｐｐｐｐｐｐｐ}}{{ああああああああ}{あああああああああああ}}"]


converte_dictionary(sample)
