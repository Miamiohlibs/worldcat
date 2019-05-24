import multiprocessing
import python.dbWriter
from python.dbWriter import dbWriter, batchStatus, create_db, connect_db, db_close

# function to withdraw from account
def withdraw(balance, read,write):
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

def perform_transactions():
    # initial balance (in shared memory)
    balance =  multiprocessing.Manager().list(thousand)
    # creating a lock object
    read = multiprocessing.Lock()
    write = multiprocessing.Lock()
    # creating new processes
    p1 = multiprocessing.Process(target=withdraw, args=(balance,read,write))
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
    for _ in range(10):
        # perform same transaction process 10 times
        perform_transactions()
