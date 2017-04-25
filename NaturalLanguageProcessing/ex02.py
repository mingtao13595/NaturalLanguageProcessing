char1 = "パトカー"
char2 = "タクシー"
char1List = list(char1)
char2List = list(char2)
charPlusList = []
for i in range(max(len(char1List),len(char1List))):
	charPlusList.append(char1List[i])
	charPlusList.append(char2List[i])
charPlus = "".join(charPlusList)
print(charPlus)
