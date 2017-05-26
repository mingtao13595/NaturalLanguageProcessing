# xmlをjsonにして読み込む

# xmlの読み込み処理
def xmlToRead(readFile):
	if __name__ == '__main__':
		rf = open(readFile, 'r')
		# print(rf)
		json_list = []
		xml_tmp_str = ''
		for line in rf:
			xml_tmp_str += line
			if re.match("</sentence>", line):
				result_xml = xmltodict.parse(xml_tmp_str)
				result_json = json.dumps(result_xml,ensure_ascii=False)
				json_list.append(result_json)
				xml_tmp_str = ''
		# print(json_list)
		return json_list

dictionary_list = xmlToRead('./file/ex40.xml')
