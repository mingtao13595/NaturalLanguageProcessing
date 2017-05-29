# coding: utf-8
import CaboCha
import re

fname        = './file/neko.txt'
fname_parsed = './file/neko.txt.cabocha'

class Morph:
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base    = base
		self.pos     = pos
		self.pos1    = pos1

	# ゲッターを定義
	def getAttribute(self):
		input_list = {"surface":self.surface, "base":self.base, "pos":self.pos, "pos1":self.pos1}
		result_list = {}

		for key,value in input_list.items():
			result_list[key] = value
		return result_list

def read_and_parse():
	with open(fname) as data_file, open(fname_parsed, mode='w') as out_file:
		cabocha = CaboCha.Parser()
		for line in data_file:
			out_file.write(cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE))

def article_shaping():
	with open(fname_parsed) as file_parsed:
		chunks = []
		idx    = -1

		count  = 0
		for line in file_parsed:
			result_list = {}
			if line == 'EOS\n':
				result_list = {}
				del result_list
				count += 1
				# break
			elif re.match(r'\*', line) is None:
				repl_line = re.sub(r'\t', ',', line)
				repl_line = re.sub(r'\n', '', repl_line)
				repl_list = repl_line.split(',')
				morph = Morph(repl_list[0], repl_list[7], repl_list[1], repl_list[2])
				# 表示箇所
				if count == 3:
					print(morph.getAttribute())
				chunks.append(morph)

read_and_parse()

article_shaping()
