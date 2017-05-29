# coding: utf-8
import CaboCha
import re

fname        = './file/neko.txt'
fname_parsed = './file/neko.txt.cabocha'

# Morphの構造体（Cの意味）定義
class Morph:
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base    = base
		self.pos     = pos
		self.pos1    = pos1

	def __str__(self):
		return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'.format(self.surface, self.base, self.pos, self.pos1)

# Chunkの構造体（Cの意味）定義
class Chunk:
	def __init__(self):
		self.morphs = []
		self.srcs   = []
		self.dst    = -1

	def __str__(self):
		surface = ''
		for morph in self.morphs:
			surface += morph.surface
		return '{}\tsrcs{}\tdst[{}]'.format(surface, self.srcs, self.dst)

def read_and_parse():
	with open(fname) as data_file, open(fname_parsed, mode='w') as out_file:
		cabocha = CaboCha.Parser()
		for line in data_file:
			out_file.write(
				cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE)
			)

def article_lines():
	with open(fname_parsed) as file_parsed:
		chunks = {}
		idx    = -1

		for line in file_parsed:
			if line == 'EOS\n':
				if len(chunks) > 0:
					sorted_tuple = sorted(chunks.items(), key=lambda x: x[0])
					yield list(zip(*sorted_tuple))[1]
					chunks.clear()
				else:
					yield []
			elif line[0] == '*':
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
				cols     = line.split('\t')
				res_cols = cols[1].split(',')
				chunks[idx].morphs.append(
					Morph(
						# surface
						cols[0],
						# base
						res_cols[6],
						# pos
						res_cols[0],
						# pos1
						res_cols[1]
					)
				)
		raise StopIteration

read_and_parse()

for i, chunks in enumerate(article_lines(), 1):
	if i == 8:
		for j, chunk in enumerate(chunks):
			print('[{}]{}'.format(j, chunk))
		break
