import csv
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

with open("Data/test.csv", 'a') as out:
    write = csv.writer(out, delimiter=',', quotechar='"', lineterminator='\n')
    row = next(write)
    row.append('0')
    row.append ('1')

