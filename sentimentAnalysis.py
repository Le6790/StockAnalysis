from nltk import word_tokenize
import collections
import math
import os
import csv
'''
Main program, run webscraping/main.py -> stockAnalysis/csvTokenize.py -> stockAnalysis/sentimentAnalysis.py


'''



#dates of the input 
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


#positive training text
with open("TrainingText/cleaned_positive.txt", "r", encoding="utf8") as fin:
	textPositive = fin.read()

#negative training text
with open("TrainingText/cleaned_negative.txt", "r", encoding="utf8") as fin:
	textNegative = fin.read()

#tokenize the lists 

positiveList = word_tokenize(textPositive)
negativeList = word_tokenize(textNegative)
#count the word frequencies
cPositive = collections.Counter(positiveList)
cNegative = collections.Counter(negativeList)


cAll = cPositive + cNegative

#take the filtered head and body text data and run it through naive bayes, 
#calculating a total sentiment value for each text sentence.
# Average that sentiment value and store it into ____TotalSentiment.csv 
 

def processData(dates): #list of dates to process
	#read in one line at a time
	for date in dates: 
		print(date)

		if os.path.isfile("Data/Head%s.csv"%(date)):
			with open("Data/Head%s.csv"%(date), 'r', encoding="utf8") as fin:
				headStr = csv.reader(fin, delimiter=',')
				totalSent = 0
				count = 0
				for str1 in headStr:
					count  = count+1
					print(str1[0])
					totalSent += AssignDocumentToClass(str1[0],cPositive,cNegative, cAll)
				print("SENTIMENT:" + str(totalSent))
				outputSentiment(totalSent, date, "Head")

		if os.path.isfile("Data/Body%s.csv"%(date)):
			with open("Data/Body%s.csv"%(date), 'r', encoding="utf8") as fin:
				bodyStr  = csv.reader(fin, delimiter=',')
				totalSent = 0
				count = 0
				for str1 in bodyStr:
					count  = count+1
					#print(str1[0])
					totalSent += AssignDocumentToClass(str1[0],cPositive,cNegative, cAll)
				print("SENTIMENT:" + str(totalSent))
				outputSentiment(totalSent, date, "Body")
		else:
			print("No file. Break")
			break
		#print(headStr)

		
		#process the strings 


#writes the date as well as the sentiment total value out to a csv file for further processing 
		
def outputSentiment(sentVal, date, typeof ): #sentiment value of data, date of data
	if typeof == "Head":
		with open("Data/HeadTotalSentiment.csv", 'a', encoding="utf8") as fout:
			write = csv.writer(fout, delimiter = ',', lineterminator = '\n')
			write.writerow([date,sentVal])
    #write to overall dates csv containing all dates and the average value 
	if typeof == "Body":
		with open("Data/BodyTotalSentiment.csv", 'a', encoding="utf8") as fout:
			write = csv.writer(fout, delimiter = ',', lineterminator = '\n')
			write.writerow([date,sentVal])

###
#Naive Bayes algorithm 
###


#Give the two classes equal probabilities
def PofClass(c):
	#print("Class probability: " + str(sum(c.values())/sum(cAll.values())))
	#return sum(c.values())/sum(cAll.values())
	return 0.5

def PofTermGivenClass(t,c,cAll):
	return(c[t.lower()] + 1)/ (sum(c.values())+ len(cAll))

def AssignDocumentToClass(d,c1,c2,cAll):
	W = d.lower().split()
	sum1 = PofClass(c1)#+0.005
	for w in W:
		sum1 = sum1 + math.log10(PofTermGivenClass(w,c1,cAll))
	sum2 = PofClass(c2)
	for w in W:
		sum2 = sum2 + math.log10(PofTermGivenClass(w,c2,cAll))

	if (sum1 > sum2):
		print("Positive: " + str(sum1))
		print("Negative: " + str(sum2))
		
		print("********************positive Sentiment by: " + str (sum1-sum2))
		return sum1-sum2

	else:
		print("Positive: " + str(sum1))
		print("Negative: " + str(sum2))
		print("----------------Negative Sentiment by: " + str(sum1-sum2))
		return sum1 - sum2

def main():
	processData(dates)


if __name__ == "__main__":
	main()