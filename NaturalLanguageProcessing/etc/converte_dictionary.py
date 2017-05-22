#!/usr/bin/env python
# coding: UTF-8
import re
import copy

# repatter = re.compile('\{')

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

		for line in str_list:
			print(line)

			# matchOB = re.match('\{' , char)
			#
			# brace_list = char[:-1].split('{')
			#
			# result_dictionary.append(new_line_list)


# sample = ["{{AAA},aaaaaaa}aaaa", "{{ｐｐｐｐｐｐ}, {ｐｐｐｐｐｐｐｐｐ}}", "{{ああああああああ},{あああああああああああ}}"]

sample = ["{{AAA},aaaaaaa}{{ｐｐｐｐｐｐ} {ｐｐｐｐｐｐｐｐｐ}}{{ああああああああ}{あああああああああああ}}"]


converte_dictionary(sample)
