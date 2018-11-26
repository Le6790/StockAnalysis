import string
from nltk import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))
translate_table = dict((ord(char), None) for char in string.punctuation)  


def filterText(textInput): #input: file path
    with open(textInput, 'r') as infile:
        data = infile.read().lower()

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
            finalData.append(w)

    
    
    print(finalData)
    
    #TODO *automate
    #Write to a file 
    with open("TrainingText/"+"cleaned_positive.txt", "w") as file:
        for w in finalData:
            file.write(w + " ")



filterText("TrainingText/positive.txt")

