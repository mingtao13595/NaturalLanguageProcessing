# coding: utf-8
#!/usr/bin/env python

import CaboCha

fname        = './file/neko.txt'
fname_parsed = './file/neko.txt.cabocha'

class Morph:
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base    = base
		self.pos     = pos
		self.pos1    = pos1

	def __str__(self):
		return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'.format(self.surface, self.base, self.pos, self.pos1)

class Chunk:
	def __init__(self, morph, dst, srcs):
		self.morph = morph
		self.dst   = dst
		self.srcs  = srcs

	def __str__(self):
		return 'morph[{}]\tdst[{}]\tsrcs[{}]'.format(self.morph, self.dst, self.srcs)


def read_and_parse():
	with open(fname) as data_file, open(fname_parsed, mode='w') as out_file:
		cabocha = CaboCha.Parser()
		for line in data_file:
			# out_file.write(cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE))
			out_file.write(cabocha.parse(line).toString(CaboCha.FORMAT_XML))

def article_lines():
	with open(fname_parsed) as file_parsed:
		morphs = []
		xml_tmp_str = ''
		for line in file_parsed:
			xml_tmp_str += line
			if re.match("</sentence>", line):
				result_xml = xmltodict.parse(xml_tmp_str)
				xml_tmp_str = ''



			if line == 'EOS\n':
				yield morphs
				morphs = []
			else:
				if line[0] == '*':
					continue
				cols = line.split('\t')
				res_cols = cols[1].split(',')
				morphs.append(Morph(
					cols[0],
					res_cols[6],
					res_cols[0],
					res_cols[1]
				))
		raise StopIteration

read_and_parse()
for i, morphs in enumerate(article_lines(), 1):
	if i == 8:
		for morph in morphs:
			print(morph)
		break
