# n-gram
def bi_gram(gramElementList):
	word_bi_gramList = []
	for i in range(len(gramElementList)):
		# 文字列が最大に達したときにloopを抜ける
		if i+1 == len(gramElementList):
			return word_bi_gramList
		# bi-gram生成
		word_bi_gramList.append(gramElementList[i]+"-"+gramElementList[i+1])

def word_bi_gram(sentence):
	wordList = sentence.split(" ")
	return bi_gram(wordList)

def char_bi_gram(sentence):
	sentence_deleteSpace = sentence.strip()
	# 全角空白削除
	sentence_deleteSpace = sentence_deleteSpace.replace("　","")
	# 半角空白削除
	sentence_deleteSpace = sentence_deleteSpace.replace(" ","")
	return bi_gram(sentence_deleteSpace)

sentence = "I am an NLPer"
print(word_bi_gram(sentence))
print(char_bi_gram(sentence))
