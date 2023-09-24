import sqlite3
from collections import namedtuple


class TableData:
    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name

    def get_db_tables_list(self):
        with sqlite3.connect(self.database_name) as connection:
            # cursor is an object that allows you to interact with a database result set. It acts as an iterator
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            table_names = cursor.fetchall()

            table_names = [table[0] for table in table_names]
            return table_names

    def get_table_data(self):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f'SELECT * from {self.table_name}')
            data = cursor.fetchall()
            return data

    def __len__(self):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f'SELECT count(*) from {self.table_name}')
            return cursor.fetchone()[0]

    def __getitem__(self, item):
        for getitem_row in self.get_table_data():
            if getitem_row[1] == item:
                return {'title': getitem_row[0], 'author': getitem_row[1]}

    def __contains__(self, item):
        for contains_row in self.get_table_data():
            if contains_row[1] == item:
                return True
        return False

    def __iter__(self):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f'SELECT * from {self.table_name}')
            while True:
                row_in_table = cursor.fetchone()
                if row_in_table is None:
                    break
                yield {'title': row_in_table[0], 'author': row_in_table[1]}


if __name__ == "__main__":
    books_table = TableData('example.sqlite', 'books')
    rows = books_table.get_table_data()
    for row in rows:
        print(row)
    print()
    print(len(books_table))
    print(books_table['Bradbury'])
    print('Yeltsin' in books_table)
    print('Bradbury' in books_table)
    for book in books_table:
        print(book['author'])


# Write a wrapper class TableData for database table, that when initialized with database name and table
# acts as collection object (implements Collection protocol).
# Assume all data has unique values in 'author' column.
# So, if books = TableData(database_name='example.sqlite', table_name='books')
#
# then
#  -  `len(books)` will give current amount of rows in books table in database
#  -  `books['Bradbury']` should return single data row for book with author Bradbury
#  -  `'Yeltsin' in books` should return if book with same author exists in table
#  -  object implements iteration protocol. i.e. you could use it in for loops::
#        for book in books:
#            print(book['author'])
#  - all above mentioned calls should reflect most recent data.
#  If data in table changed after you created collection instance, your calls should return updated data.
#
# Avoid reading entire table into memory. When iterating through records, start reading the first record, then go to the next one, until records are exhausted.
# When writing tests, it's not always necessary to mock database calls completely. Use supplied example.sqlite file as database fixture file.
