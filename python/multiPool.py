import multiprocessing

# function to withdraw from account
def withdraw(balance, lock):
# def read(balance,lock): #read lock
    lock.acquire()
    del balance[:1]
    lock.release()

# function to deposit to account
def deposit(balance, lock):
# def dbWriter(batch,dbName,lock): #write lock
    lock.acquire()
    del balance[:1]
    lock.release()

def perform_transactions():
    # initial balance (in shared memory)
    balance =  multiprocessing.Manager().list(results)
    # creating a lock object
    lock = multiprocessing.Lock()
    # write = multiprocessing.Lock()
    # creating new processes
    p1 = multiprocessing.Process(target=withdraw, args=(balance,lock))
    p2 = multiprocessing.Process(target=deposit, args=(balance,lock))
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
