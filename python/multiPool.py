import multiprocessing
import python.dbWriter
from python.dbWriter import dbWriter, batchStatus, create_db, connect_db, db_close

# function to withdraw from account
def withdraw(balance,read,write):
# def read(balance,lock): #read lock
    while balance:
        read.acquire()
        fifty = balance[:50]
        del balance[:50]
        read.release()
        print(len(fifty))
        batch = batchStatus(fifty)
        write.acquire()
        dbWriter(batch,dbName)
        write.release()
        del fifty[:50]
        print(len(balance))

def perform_transactions(): #define hundred, dbName
    # initial balance (in shared memory)
    balance =  multiprocessing.Manager().list(hundred)
    # creating a lock object
    read = multiprocessing.Lock()
    write = multiprocessing.Lock()
    # creating new processes
    p1 = multiprocessing.Process(target=withdraw, args=(balance,read,write)) #add dbName
    p2 = multiprocessing.Process(target=withdraw, args=(balance,read,write))
    # starting processes
    p1.start()
    p2.start()
    # wait until processes are finished
    p1.join()
    p2.join()
    # print final balance
    return balance

if __name__ == "__main__":
    perform_transactions() #need to pass in predefined vars below
    # hundred = main(passwd,sqlName()) and dbName = 'test'
