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
            # c.execute('CREATE TABLE IF NOT EXISTS test(oclc,status)')
            try:
                c.execute("INSERT INTO test VALUES({},{})".format(i,test))
                conn.commit()
                print('db write successful')
            except:
                print('db write failed')
        except:
            ('nothing worked, throwing in the towel')
        wait = uniform(.2,2)
        time.sleep(wait)
        # mul.append([i,test])
        # print(len(mul))



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
