import sqlite3

class DB:
    def __init__(self, path):
        try:
            self.connection = sqlite3.connect(path)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(e)

    def get_all(self) -> list:
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()

    def get_name(self) -> list:
        self.cursor.execute("SELECT nome FROM usuarios")
        return self.cursor.fetchall()

    def get_votes(self) -> list:
        self.cursor.execute("SELECT vote FROM usuarios")
        return self.cursor.fetchall()

    def get_position(self) -> list:
        self.cursor.execute("SELECT postion FROM usuarios")
        return self.cursor.fetchall()

    def search_name(self, term:str) -> list:
        term = term + "%"
        self.cursor.execute('''
            SELECT * FROM usuarios 
            WHERE nome LIKE ?''', (term,))
        return self.cursor.fetchall()

    def seach_vote(self, term:int) -> list:
        self.cursor.execute('''
            SELECT * FROM usuarios
            WHERE vote = ?
        ''', (term,))
        return self.cursor.fetchall()

    def search_position(self, term:int) -> list:
        self.cursor.execute('''
            SELECT * FROM usuarios
            WHERE position = ?
        ''', (term,))
        return self.cursor.fetchall()

    def search_repo(self, term:str) -> list:
        term = "%" + term + "%"
        self.cursor.execute('''
            SELECT * FROM usuarios
            WHERE link LIKE ?
        ''', (term,))
        return self.cursor.fetchall()

