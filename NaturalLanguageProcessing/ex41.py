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

# Chunkの構造体（Cの意味）定義
class Chunk:
	def __init__(self):
		self.morphs = []
		self.srcs   = []
		self.dst    = -1

def read_and_parse():
	with open(fname) as data_file, open(fname_parsed, mode='w') as out_file:
		cabocha = CaboCha.Parser()
		for line in data_file:
			out_file.write(
				cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE)
			)

def article_shaping():
	with open(fname_parsed) as file_parsed:
		chunks = {}
		idx    = -1
		for line in file_parsed:
			print(line)

# read_and_parse()

article_shaping()
