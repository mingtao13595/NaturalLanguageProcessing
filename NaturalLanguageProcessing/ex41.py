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

class Chunk:
	def __init__(self):
		self.morphs = []
		self.srcs   = []
		self.dst    = -1

	# セッターを定義
	def setAttribute(self, morphs):
		self.morphs = morphs

	# セッターを定義
	def setAttribute_srcs(self, srcs, dst):
		self.srcs   = srcs
		self.dst    = dst

	# ゲッターを定義
	def getAttribute(self):
		input_list = {"morphs":self.morphs, "srcs":self.srcs, "dst":self.dst}
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
		morphs = []

		for line in file_parsed:
			if line == 'EOS\n':
				chunk = Chunk()
				chunk.setAttribute(morphs)
				chunks.append(chunk)
				morphs = []
			elif re.match(r'\*', line) is not None:
				pass
				cols = line.split(' ')
				idx  = int(cols[1])
				dst  = int(re.search(r'(.*?)D', cols[2]).group(1))
				if dst != -1:
					chunk.setAttribute_srcs(dst,idx)
			else:
				repl_line = re.sub(r'\t', ',', line)
				repl_line = re.sub(r'\n', '', repl_line)
				repl_list = repl_line.split(',')
				morph = Morph(repl_list[0], repl_list[7], repl_list[1], repl_list[2])
				morphs.append(morph)
		return chunks

# read_and_parse()

chunks = article_shaping()

count = 0
for chunk in chunks:
	if count == 7:
		morphs = chunk.getAttribute()['morphs']
		for morph in morphs:
			print(morph.getAttribute())
		break
	count += 1