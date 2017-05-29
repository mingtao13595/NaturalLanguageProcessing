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

	def setAttribute(self, morphs):
		surface = ''
		for morph in self.morphs:
			surface += morph.surface

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
		chunks = {}
		chunk  = []
		idx    = -1

		for line in file_parsed:
			result_list = {}
			if line == 'EOS\n':
				result_list = {}
				chunks.append(chunk)
				del result_list
				chunk = []
			elif re.match(r'\*', line) is not None:
				cols = line.split(' ')
				idx  = int(cols[1])
				dst  = int(re.search(r'(.*?)D', cols[2]).group(1))
				if idx not in chunks:
					chunks[idx] = Chunk()
				chunks[idx].dst = dst
				if dst != -1:
					if dst not in chunks:
						chunks[dst] = Chunk()
						chunks[dst].srcs.append(idx)
			else:
				repl_line = re.sub(r'\t', ',', line)
				repl_line = re.sub(r'\n', '', repl_line)
				repl_list = repl_line.split(',')
				morph = Morph(repl_list[0], repl_list[7], repl_list[1], repl_list[2])
				chunk.append(morph)
		return chunks

# read_and_parse()

chunks = article_shaping()
count  = 0

for k, chunk in chunks.item():
	if count == 8:
		for line in chunk:
			print(line.getAttribute())
		break
	count += 1
