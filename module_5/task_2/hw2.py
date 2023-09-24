import sqlite3


class TableData:
    def __init__(self, database_name: str, table_name: str = None):
        self.database_name = database_name
        if table_name:
            self.table_name = table_name
        else:
            self.table_name = self.get_db_tables_list()[0]

    def get_db_tables_list(self):
        with sqlite3.connect(self.database_name) as connection:
            # cursor is an object or data structure that allows you to interact with a database result set.
            # It acts as a pointer or iterator
            # that helps you navigate through the rows of data retrieved from a database query
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            table_names = cursor.fetchall()

            cursor.close()
            connection.close()

            table_names = [table[0] for table in table_names]
            return table_names

    def get_table_data(self, table_name: str = None):
        if not table_name:
            table_name = self.table_name
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f'SELECT * from {table_name}')
            data = cursor.fetchall()
            return data


if __name__ == "__main__":
    table_data = TableData('example.sqlite', 'books')
    rows = table_data.get_table_data()
    for row in rows:
        print(row)
