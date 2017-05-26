# xmlをjsonにして読み込む

import MeCab
import CaboCha
import re
import json
import xmltodict

# xmlの変換処理
def textToXML(readFile, writeFile):
	f  = open(readFile, 'r')
	wf = open(writeFile, 'a')

	mt = CaboCha.Parser()
	for line in f:
		tree = mt.parse(line)
		wf.write(tree.toString(CaboCha.FORMAT_XML))

# xmlの読み込みjsonで書き出す処理
def xmlToJson(readFile, writejsonFile):
	if __name__ == '__main__':
		# print(readFile)
		rf = open(readFile, 'r')
		wf = open(writejsonFile, 'a')
		# print(rf)
		json_list = []
		xml_tmp_str = ''
		wf.write("[\n")
		for line in rf:
			xml_tmp_str += line
			if re.match("</sentence>", line):
				result_xml = xmltodict.parse(xml_tmp_str)
				result_json = json.dumps(result_xml, indent='\t', ensure_ascii=False, sort_keys=True, separators=(',', ': '))
				wf.write(result_json)
				wf.write(",\n")
				# json_list.append(result_json)
				xml_tmp_str = ''
		# print(type(json_list))
		# return json_list
		json.dump({"end":"終"}, wf, ensure_ascii=False, indent='\t', sort_keys=True, separators=(',', ': '))
		wf.write("\n]")


# xmlの読み込みjsonで書き出す処理
def JsonToRead(readFile):
	try:
		# ローカルJSONファイルの読み込み
		with open(readFile, 'r') as rf:
			data = json.load(rf)
			return data
	except json.JSONDecodeError as e:
		print('JSONDecodeError: ', e)


class Morph:
	# セッター
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base    = base
		self.pos     = pos
		self.pos1    = pos1

	# ゲッター
	def __str__(self):
		return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'\
		.format(self.surface, self.base, self.pos, self.pos1)

# cobachaで出されたものをxmlにして、吐き出す
# textToXML('./file/neko.txt', './file/ex40.xml')
# xmlをjsonに変換して吐き出す
# xmlToJson('./file/ex40.xml', './file/ex40.json')
# jsonをdcitionaryにして受け取る
dict_list = JsonToRead('./file/ex40.json')
print(dict_list)

# # インスタンス生成
# morph = Morph
# morph.surface = dictionary_list[3]
# morph.base    = dictionary_list[3]
# morph.pos     = dictionary_list[3]
# morph.pos1    = dictionary_list[3]
#
# print(morph)
