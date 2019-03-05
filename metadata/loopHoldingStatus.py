import csv, holdingStatus
from holdingStatus import status

with open('sandboxRecords.csv') as file:
    readCSV = csv.reader(file)
    for row in readCSV:
        print(row, status(row))

file.close()
