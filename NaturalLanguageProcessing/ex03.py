char = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
charWordList = char.split(" ")
numList = []
for i in range(len(charWordList)):
	numList.append(len(charWordList[i]))
print(numList)
