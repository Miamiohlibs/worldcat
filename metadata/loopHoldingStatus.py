#purpose of looping through csv list of records

def loopHolding():
    import csv, holdingStatus, re
    from holdingStatus import status

    with open('../data/sandboxRecords.csv') as file:
        data = list(csv.reader(file))

    for i in data:
        for s in range(len(data)):
            number = re.sub("[^0-9]","",data[s][0]) #takes out any characters

                #check to make sure oclcnumb is correct length
                #if len(number) !=
            holding = status(number)
            #if holding = False:
                #updateHolding(number)
            #elif holding = True:
                #Something
            #else:
                #nothing
            print(s,number,holding) #dev testing variables
        if s == len(data)-1:
            break
    print("stop")
