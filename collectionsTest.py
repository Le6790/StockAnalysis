import collections
from nltk import word_tokenize
with open("TrainingText/cleaned_positive.txt", "r") as fin:
	textPositive = fin.read()
with open("TrainingText/cleaned_negative.txt", "r") as fin:
	textNegative = fin.read()



#tokenize the lists 

positiveList = word_tokenize(textPositive)
negativeList = word_tokenize(textNegative)

#count the word frequencies
cPositive = collections.Counter(positiveList)
cNegative = collections.Counter(negativeList)


cAll = cPositive+cNegative
print(cAll)
print(cAll['my'])
print(len(cAll))

k = 0
for x in cAll:
	k += cAll[x]

print(k)


def PofC(c):
	print(c.values())
	print(cAll.values())
	return sum(c.values())/sum(cAll.values())

print(PofC(cPositive))
print(PofC(cNegative))

print(cPositive.most_common(10))
print("------------------------------")
print(cNegative.most_common(10))


# print(cPosiStive)
# print("==========================")
# print(cNegative)


