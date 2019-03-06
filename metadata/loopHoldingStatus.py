import csv, holdingStatus
from holdingStatus import status

with open('../data/sandboxRecords.csv') as file:
    data = list(csv.reader(file))

counter = 0
for i in data:
    #check to make sure oclcnumb is correct length
    number = data[counter][0]
    holding = status(number)
    print(number,holding)
    counter += 1 #probably a better way to do counter

    #if holding = False:
        #updateHolding(number)
    #elif holding = True:
        #Something
    #Else:
        #nothing
