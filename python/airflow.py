def oclcFlow(filename):
    import sqlite3

    sql_command = sqlImport(filename)


def sqlImport(sqlName):
    with open('../sql/'+sqlName, 'r') as f:
        content = f.read()
        content = content.replace('\n',' ')
        f.close()
    return content
    #not returning exact file contents
