import string
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
stop_words = set(stopwords.words("english"))
translate_table = dict((ord(char), None) for char in string.punctuation)  

ps = PorterStemmer()

def filterText(textInput): #input: file path
    with open("TrainingText/%s.txt"%(textInput), 'r', encoding="utf8") as infile:
        #data = line.strip() for line in infile
        data = infile.read().lower()

    print(data)
    #remove punctuation
    data = data.translate(translate_table)
    data = data.replace("’", "") #different character than '
    data = data.replace("“", "") #different character than "

    #Word Tokenize the data
    words = word_tokenize(data) 

    #remove stop words
    finalData = []
    for w in words:
        if w not in stop_words:
            finalData.append(ps.stem(w))

    
    
    print(finalData)
    
    #TODO *automate
    #Write to a file 
    with open("TrainingText/cleaned_%s.txt"%(textInput), "w", encoding="utf8") as file:
        for w in finalData:
            file.write(w + " ")



filterText("negative")

