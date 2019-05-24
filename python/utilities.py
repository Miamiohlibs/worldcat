# collection of functions to parse Sierra sql data and check OCLC holdings

def sqlImport(sqlName):
    # opens a local saved .sql file and returns the query
    # query must be in a minified format without carriage returns or comments
    with open('sql/'+sqlName, 'r', encoding='utf-8-sig') as f:
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
