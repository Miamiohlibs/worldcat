def dbWriter(results):
    from random import uniform
    import sqlite3, time, datetime
    from stati.holdingStatus import status
    conn = sqlite3.connect('../Oxford.db')
    c = conn.cursor()
    for i in results:
        try:
            test = status(i)
            if test:
                print('status checked', test)
            else:
                print('status read failed')
        except:
            ('nothing worked, throwing in the towel')
        wait = uniform(.2,2)
        time.sleep(wait)
        # mul.append([i,test])
        # print(len(mul))
        c.execute('CREATE TABLE IF NOT EXISTS test(oclc,status)')
        # should not need to create table but it doesn't work without it
        try:
            c.execute("INSERT INTO test VALUES({},{})".format(i,test))
            conn.commit()
            print('db write successful')
        except:
            print('db write failed')


# https://python-forum.io/Thread-insert-list-into-sqlite3

def create_db():
    c.execute('CREATE TABLE IF NOT EXISTS test(oclc,status)')

def data_entry(i):
    c.execute("INSERT INTO test VALUES({},{})".format(i[0],i[1]))
    conn.commit()
    # c.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%m-%d'))
    value = random.randrange(0,len(words))
    c.execute("INSERT INTO foobar (unix,datestamp,value) VALUES(?,?,?)",
    (unix, date, value))
    conn.commit()

def db_close(c, conn):
    c.close()
    conn.close()

def multi(one,two):
    import multiprocessing
    # creating processes
    p1 = multiprocessing.Process(target=dbWriter, args=(one[:3], ))
    p2 = multiprocessing.Process(target=dbWriter, args=(two[:3], ))
    # starting process 1
    p1.start()
    # starting process 2
    p2.start()
    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()
    # both processes finished
    print("Done!")

if __name__ == "__main__":
    one = ['27429232', '32778355', '968141', '39381268', '7119961', '575236', '16715413', '558486', '774160330', '7430088']
    two = ['17257924', '13845695', '21972508', '48070545', '34281492', '52511400', '51182403', '43396865', '48195094', '32075467']
    #dbWriter(one)
    multi(one,two)
