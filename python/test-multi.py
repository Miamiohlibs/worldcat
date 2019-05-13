import sqlite3
import multiprocessing
'''
This program starts a daemon process that listens on a queue.
It then starts 10 processes that place integers in the queue.
The listening daemon pulls the integers out of the queue and
stores them in the database.

https://gist.github.com/cessor/f8bf530212fbe75263c79564f5fc15ad
'''
DB_FILENAME = 'db.sqlite'


class DbCommands(object):
    CLEAR = 'delete from test'
    DROP = 'drop table if exists test'
    COUNT = 'select count(*) from test'
    INIT = 'create table if not exists test (value integer not null)'
    INSERT = 'insert into test (value) values (?)'


class Database(object):

    def __init__(self, path):
        self._path = path
        self._connection = None

    def __enter__(self):
        self._connection = sqlite3.connect(self._path)
        # Reset Database
        self.execute(DbCommands.DROP)
        self.execute(DbCommands.INIT)
        self.execute(DbCommands.CLEAR)
        return self

    def __exit__(self, *args, **kwargs):
        self._connection.commit()

    def commit(self):
        self._connection.commit()

    def execute(self, sql, *args):
        cursor = self._connection.cursor()
        if not args:
            return cursor.execute(sql)
        return cursor.execute(sql, args)


class Command(object):

    def __init__(self, *args):
        self._args = args


class Count(Command):

    def execute(self, database):
        count = database.execute(DbCommands.COUNT).fetchall()
        count = count[0][0]
        print('Count: ', count)


class Commit(Command):

    def execute(self, database):
        database.commit()
        raise Break()


class Insert(Command):

    def execute(self, database):
        database.execute(DbCommands.INSERT, *self._args)


class Break(Exception):
    pass


def handle(queue):
    with Database(DB_FILENAME) as database:
        while True:
            try:
                command = queue.get()
                command.execute(database)
                queue.task_done()

            except Break:
                queue.task_done()
                break

            except Exception as e:
                print(e)


def add_to_queue(queue):
    for i in range(100):
        queue.put(Insert(i))


def main():
    queue = multiprocessing.JoinableQueue()

    # Start a Daemon Process
    multiprocessing.Process(target=handle, args=(queue,), daemon=True).start()

    # Start Processes
    processes = [
        multiprocessing.Process(target=add_to_queue, args=(queue,))
        for _ in range(10)
    ]

    # Start Daemons
    for process in processes:
        process.start()

    # Wait until Daemons are done
    for process in processes:
        process.join()

    # Query a command to the database
    queue.put(Count())

    # Send a command to the handler
    # To commit, clean, and close the database
    queue.put(Commit())

    # Do Not Join Daemon Threads,
    # Join their Queues instead
    queue.join()


if __name__ == '__main__':
    main()
