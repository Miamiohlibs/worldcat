s to fee# collection of functions to parse Sierra sql data and check OCLC holdings

def sqlImport(sqlName):
    # opens a local saved .sql file and returns the query
    # query must be in a minified format without carriage returns or comments
    with open('../sql/'+sqlName, 'r', encoding='utf-8-sig') as f:
        content = f.read()
        content = content.replace('\n',' ')
        f.close()
    return content
    #not returning exact file contents
    # sqlName = 'mdl-min.sql'

# main() accepts sql password and minimized sql query as args
# main() parses any sql query and returns a list array for each row in result
# remove commented database criteria to establish connection
# normal sql network access limits/firewalls apply
# https://pynative.com/python-postgresql-select-data-from-table/
def main(password,sqlName):
    import psycopg2, sys
    try:
        # connection = psycopg2.connect(user = "user",
        #                               password = password,
        #                               host = "hostIP",
        #                               port = "port",
        #                               database = "db")
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
# 	main()


def sortingHat(slice):
    # parses list of OCLC numbers into good integers or bad integers if char
    for i in slice:
        try:
            good.append(int(i))
            # print('good place')
        except ValueError:
            bad.append(i)
            # print('string goes to bad place')
    return good, bad
# test criteria
# from airflow import main, sqlImport, sortingHat, shredder
# results = main('passwd', sqlImport('main-campus-min.sql'))

# slice = ['28633839', '29260', '21972508', '12555624', '32609688', '32075467', '313365654', '11262171', '28384097', '18886825', '13409asdf']
# good,bad = sortingHat(results)

# if __name__ == "__main__":
def shredder(queue1,queue2):
    import threading
    good,bad = [],[]
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))

    # print name of main thread
    print("Main thread name: {}".format(threading.main_thread().name))

    # creating threads
    t1 = threading.Thread(target=sortingHat, name='t1', args=queue1)
    t2 = threading.Thread(target=sortingHat, name='t2', args=queue2)

    # starting threads
    t1.start()
    t2.start()

    # wait until all threads finish
    t1.join()
    t2.join()

    print(len(good),len(bad))
