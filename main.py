# accepts sql password and minimized sql query as args
# minimized being a qery without any comments or newline carriage returns
# main() parses any sql query and returns a list array for each row in result
# remove commented database criteria to establish connection
# normal sql network access limits/firewalls apply
# https://pynative.com/python-postgresql-select-data-from-table/

# imports the postgres results for all oclc numbers matching sql location code
# results = main('passwd', 'mul-min.sql')
def main(password,sqlName):
    import psycopg2, sys
    from python import utilities
    from python.utilities import sqlImport

    sqlName = sqlImport(sqlName)
    try:
        # uncomment connection() lines below replacing with your local Sierra credentials
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

if __name__ == "__main__":
	# results = main(args,kwargs)
    main()
