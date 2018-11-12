from nltk import word_tokenize
import collections
import math

#Kent Le cs4320 Stock Analysis Project
#adaptation of Douglas Galarus Classify Project Comments 

with open("positiveTokenized.txt", "r") as fin:
	textPositive = fin.read()


with open("negativeTokenized.txt", "r") as fin:
	textNegative = fin.read()

#tokenize the lists 

positiveList = word_tokenize(textPositive)
negativeList = word_tokenize(textNegative)
#count the word frequencies
cPositive = collections.Counter(positiveList)
cNegative = collections.Counter(negativeList)


cAll = cPositive + cNegative

#Give the two classes equal probabilities
def PofClass(c):
	return 0.5

def PofTermGivenClass(t,c,cAll):
	return(c[t.lower()] + 1)/ (sum(c.values())+ len(cAll))

def AssignDocumentToClass(d,c1,c2,cAll):
	W = d.lower().split()
	sum1 = PofClass(c1)
	for w in W:
		sum1 = sum1 + math.log10(PofTermGivenClass(w,c1,cAll))
	sum2 = PofClass(c2)+.05
	for w in W:
		sum2 = sum2 + math.log10(PofTermGivenClass(w,c2,cAll))

	if (sum1 > sum2):
		print("Positive: " + str(sum1))
		print("Negative: " + str(sum2))
		if (sum1-sum2 <.005):
			print("Neutral Sentiment")
		else:
			print("positive Sentiment by: " + str (sum1-sum2))
	else:
		print("Positive: " + str(sum1))
		print("Negative: " + str(sum2))
		if (sum2-sum1 <.005):
			print("Neutral Sentiment")
		else:
			print("Negative Sentiment by: " + str(sum2-sum1))


while(True):

	str1 = input("Enter a sentence to analyze (q to quit): ")

	if str1.strip().lower() == "q":
		break
	AssignDocumentToClass(str1,cPositive,cNegative, cAll)