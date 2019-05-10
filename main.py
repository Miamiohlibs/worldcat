# accepts sql password and minimized sql query as args
# main() parses any sql query and returns a list array for each row in result
# remove commented database criteria to establish connection
# normal sql network access limits/firewalls apply
# https://pynative.com/python-postgresql-select-data-from-table/

# test criteria
    # results = main('passwd', sqlImport('main-campus-min.sql'))

def main(password,sqlName):
    import psycopg2, sys
    from python.utilities import sqlImport

    sqlName = sqlImport(sqlName)
    try:
        connection = psycopg2.connect(user = "user",
                                      password = password,
                                      host = "hostIP",
                                      port = "port",
                                      database = "db")
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")
        # Print PostgreSQL version
        cursor.execute(sqlName)
        # cursor.execute("SELECT * FROM sierra_view.item_record LIMIT 100;")
        records = cursor.fetchall()
        # print("You are connected to - ", record,"\n")
        results = []
        for row in records:
           #print("Item", row, "\n")
           results.append(row[0])
        return results
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

# if __name__ == "__main__":
# 	results = main(args,kwargs)
import time
from random import uniform
import sqlite3, time, datetime
for i in results:
    test = status(i)
    mul.append([i,test])
    print(len(mul))
    wait = uniform(.2,3)
    time.sleep(wait)

# https://python-forum.io/Thread-insert-list-into-sqlite3
conn = sqlite3.connect('Oxford.db')
c = conn.cursor()

def create_db():
    c.execute('CREATE TABLE IF NOT EXISTS mul(oclc,status)')

def data_entry(i):
    c.execute("INSERT INTO mul VALUES({},{})".format(i[0],i[1]))
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
