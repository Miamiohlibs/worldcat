# collection of functions to parse Sierra sql data and check OCLC holdings

def sqlImport(sqlName):
    # opens a local saved .sql file and returns the query
    # query must be in a minified format without carriage returns or comments
    with open('/sql/'+sqlName, 'r', encoding='utf-8-sig') as f:
        content = f.read()
        content = content.replace('\n',' ')
        f.close()
    return content
    #not returning exact file contents
    # sqlName = 'mdl-min.sql'


def sortingHat(slice):
    # parses list of OCLC numbers into good integers or bad integers if char
    good,bad = [],[]
    for i in slice:
        try:
            good.append(int(i))
            # print('good place')
        except ValueError:
            bad.append(i)
            # print('string goes to bad place')
    return good, bad
    print(good, bad)
# test criteria
    # results = main('passwd', sqlImport('main-campus-min.sql'))

# slice = ['28633839', '29260', '21972508', '12555624', '32609688', '32075467', '313365654', '11262171', '28384097', '18886825', '13409asdf']
# good,bad = sortingHat(results)

def shredder(passwd):
    import threading, os
    good,bad = [],[]

    results = main(passwd, sqlImport('main-campus-min.sql'))

    queue1 = results[:50]
    queue2 = results[50:100]

    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))

    # print name of main thread
    print("Main thread name: {}".format(threading.main_thread().name))

    # creating threads
    t1 = threading.Thread(target=sortingHat, name='t1', args=(queue1,))
    t2 = threading.Thread(target=sortingHat, name='t2', args=(queue2,))

        # starting threads
    t1.start()
    t2.start()

    # wait until all threads finish
    t1.join()
    t2.join()

    # print(len(good),len(bad))

    # return(good,bad)

if __name__ == "__main__":
    import sys
    passwd = sys.argv[1]
    shredder(passwd)
