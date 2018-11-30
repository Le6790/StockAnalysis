from newspaper import Article
import csv
#https://www.google.com/search?q=dow+jones+stock&num=30&tbs=cdr:1,cd_min:10/1/2018,cd_max:10/1/2018&source=lnms&tbm=nws

url = "https://www.npr.org/2018/10/01/653430412/general-electric-stuns-wall-street-by-firing-ceo-john-flannery-after-a-year"

article = Article(url, language="en")

article.download()
article.parse()
#print(article.html)
#print(article.text)

def getArticles(dates):
    for date in dates:
        with open("urls/urls%s.csv"%(date), 'r', encoding="utf8") as csvIN:
            text = csv.reader(csvIN, delimiter=',')

            for t in text:
                #print(t)
                str1 = t[0]
                print(str1)

                article = Article(str1, language="en")
                article.download() 
                article.parse() 
                head = article.title
                body = article.text
                createRawData(head,body,date)
                

def createRawData(head,body, date):
    with open("Data/raw%s.csv"%date, 'a', encoding = "utf8") as fout:
        write = csv.writer(fout, delimiter=',',lineterminator='\n')
        write.writerow([head, body])

getArticles(["10-01-18"])