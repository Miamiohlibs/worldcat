import csv, holdingStatus
from holdingStatus import status

with open('../data/sandboxRecords.csv') as file:
    data = list(csv.reader(file))

for i in data:
    #check to make sure oclcnumb is correct length

    counter = 0
    status(data[counter][0])
    counter += 1

    #SUCCESS

    #include if statement that if status != TRUE, send holding update PUT request
