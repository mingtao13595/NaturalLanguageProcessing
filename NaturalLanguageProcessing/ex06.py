# 06.set
chars = ["paraparaparadise","paragraph"]

# n-gram
def bi_gram(gramElementList):
	word_bi_gramList = []
	for i in range(len(gramElementList)):
		# 文字列が最大に達したときにloopを抜ける
		if i+1 == len(gramElementList):
			return word_bi_gramList
		# bi-gram生成
		word_bi_gramList.append(gramElementList[i]+gramElementList[i+1])

def char_bi_gram(sentence):
	sentence_deleteSpace = sentence.strip()
	# 全角空白削除
	sentence_deleteSpace = sentence_deleteSpace.replace("　","")
	# 半角空白削除
	sentence_deleteSpace = sentence_deleteSpace.replace(" ","")
	return bi_gram(sentence_deleteSpace)

X = char_bi_gram(chars[0])
Y = char_bi_gram(chars[1])

# print (X)
# print (Y)

# 和集合
union = X + Y
# 重複削除
union = list(set(union))
# print (union)

# 積集合
bigset   = max(X, Y)
smallset = min(X, Y)
meet     = []
for i in range(len(bigset)):
	for j in range(len(smallset)):
		if bigset[i] == smallset[j]:
			meet.append(smallset[j])
meet = list(set(meet))
# print (meet)

# 差集合
difference = union
for j in range(len(meet)):
	difference.remove(meet[j])
# print (difference)
