#purpose of looping through csv list of records

def loopHolding():
    import csv, holdingStatus
    from holdingStatus import status

    with open('../data/sandboxRecords.csv') as file:
        data = list(csv.reader(file))

    for i in data:
        for s in range(len(data)):
        #check to make sure oclcnumb is correct length
            number = data[s][0]
            holding = status(number)
            print(s,number,holding)

        if s == len(data)-1:
            break
    print("stop")


    #if holding = False:
        #updateHolding(number)
    #elif holding = True:
        #Something
    #else:
        #nothing
