import string
import csv
from nltk import word_tokenize
from nltk.corpus import stopwords


''' Todo list
- Check if files exist in Data folder
- Specify which file to create
- Create that file

'''
dates = ["10-01-18",
            "10-02-18",
            "10-03-18",
            "10-04-18",
            "10-05-18",
            "10-06-18",
            "10-07-18",
            "10-08-18",
            "10-09-18",
            "10-10-18",
            "10-11-18",
            "10-12-18",
            "10-13-18",
            "10-14-18",
            "10-15-18",
            "10-16-18",
            "10-17-18",
            "10-18-18",
            "10-19-18",
            "10-20-18",
            "10-21-18",
            "10-22-18",
            "10-23-18",
            "10-24-18",
            "10-25-18",
            "10-26-18",
            "10-27-18",
            "10-28-18"]

stop_words = set(stopwords.words("english"))
translate_table = dict((ord(char), None) for char in string.punctuation)  

# import TokenizeCSV
#read in the data 



# with open("Data/10-1-18.csv") as csvFile:
#     read = csv.reader(csvFile, delimiter =',')
#     line_count = 0
    
#     c = 1
#     news = {}

#     for row in read:
               
#         news[row[0]] = row[1]

#     print(list(news.keys())[0])
#     print(list(news.values())[0])

# with open("Data/test.csv", 'a') as out:
#     write = csv.writer(out, delimiter=',', quotechar='"', lineterminator='\n')
#     row = next(write)
#     row.append('0')
#     row.append ('1')



def processData(dates):#input - list of dates
    #TODO: for date in dates...
    # 
    for date in dates: 
        with open("Data/raw%s.csv"%(date), 'r', encoding="utf8") as csvIN: #read in each data file 
            text = csv.reader(csvIN, delimiter=',')

            aHeading = []
            aBody = []

            for row in text:
                row[0] = row[0].translate(translate_table)
                row[0] = row[0].replace("’", "") #different character than '
                row[0] = row[0].replace("“", "") #different character than "
                row[1] = row[1].translate(translate_table)
                row[1] = row[1].replace("’", "") #different character than '
                row[1] = row[1].replace("“", "") #different character than "

                aHeading.append(row[0].lower())
                aBody.append(row[1].lower())

            articleHeading = []
            articleBody = []

            for w in aHeading:
                if w not in stop_words:
                    articleHeading.append(w)

            for x in aBody:
                if x not in stop_words:
                    articleBody.append(x)

            #tokenize the lists
            #print(articleHeading)
            #print(stop_words)

            tokenizedHead = []
            tokenizedBody = []
            for x in articleHeading:
                tokenizedHead.append(word_tokenize(x))
            for x in articleBody:
                tokenizedBody.append(word_tokenize(x))

            #print(tokenizedHead)
            tokenizedToCSV(tokenizedHead,date, "Head") #Change date[0]

            #tokenizedBody = word_tokenize(articleBody)

            #write tokenized head and body to a csv file for more processing. 

def tokenizedToCSV(tokenized, date, typeOf): #Input: Tokenized List, date for name entry, and typeOf(Head or Body)

    for token in tokenized: 
        str1 = ""
        for tok in token:
            str1+=(tok + " ")
        print(str1)
        
        if typeOf == "Head":
            with open("Data/Head%s.csv"%(date), 'a', encoding="utf8") as fout:
                write = csv.writer(fout, delimiter=',', quotechar='"',lineterminator='\n')
                write.writerow([str1])
        if typeOf == "Body":
            with open("Data/Body%s.csv"%(date), 'a', encoding="utf8") as fout:
                write = csv.writer(fout, delimiter=',', quotechar='"',lineterminator='\n')
                write.writerow([str1])
        
        
        
   # if typeOf == "Head":
        # with open("Data/%s.csv"%(date), 'w', encoding="utf8") as fout:
        #      write = csv.writer(fout, delimiter=',', quotechar='"', lineterminator='\n')
        #      for token in tokenized:
        #          row = next(write)
        #          row.append(token)

#assign document to class

        



def main():
    #in main program, select the dates that I want to process. For now, instead of saving sentiment value, just save it to a dictionary

    
    testDate = ["10-01-18","10-02-18"]
    processData(testDate)



if __name__ == "__main__":
    main()