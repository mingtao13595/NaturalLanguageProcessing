char = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
charWordList = char.split(" ")
charChoiceList = []
for i in range(len(charWordList)):
	tmpCharList = list(charWordList[i])
	if i == 0 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 14 or i == 15 or i == 18:
		charChoiceList.append(tmpCharList[0])
	else:
		charChoiceList.append(tmpCharList[0]+tmpCharList[1])
print(charChoiceList)
