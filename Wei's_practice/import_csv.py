import csv

csvFile = open('/Users/wei-chunhung/Desktop/Ettoday_webScraping.csv','w+', newline='')

try:
    writer = csv.writer(csvFile)
    writer.writerow(('Category','Product','Quantity'))
    writer.writerow(('iPhone','iPhone 12','20'))
finally:
    csvFile.close()