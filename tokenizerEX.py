import string
from nltk import word_tokenize 
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))
translate_table = dict((ord(char), None) for char in string.punctuation)  

filteredSentence = []
with open('negative.txt', 'r') as file:
	data = file.read().lower()
	
	data = data.translate(translate_table)
	data = data.replace("’'", "")
	#print(data)

	words = word_tokenize(data)

	for w in words:
		if w not in stop_words:
			filteredSentence.append(w)

	print(filteredSentence)

with open("negativeTokenized.txt", 'w') as file:

	for w in filteredSentence:
		file.write(w + " ")