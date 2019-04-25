def oclcFlow(filename):
    import sqlite3

    sql_command = sqlImport(filename)


def sqlImport(sqlName):
    with open('../sql/'+sqlName, 'r', encoding='utf-8-sig') as f:
        content = f.read()
        content = content.replace('\n',' ')
        f.close()
    return content
    #not returning exact file contents
    # sqlName = 'mdl-min.sql'

# def main(password):
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

def sortingHat(results):
    good,bad = [],[]
    for i in results:
        try:
            test = int(i)
            print(test)
        except ValueError:
            bad.append(i)
            print('string goes to bad place')
        except Exception:
            good.append(int(i))
            print('good place')
    return good, bad

from airflow import sortingHat
slice = ['28633839', '29260', '21972508', '12555624', '32609688', '32075467', '313365654', '11262171', '28384097', '18886825', '13409asdf']
good,bad = sortingHat(slice)
