import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("book.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT , author TEXT, year INTEGER, no INTEGER )")
        self.conn.commit()


    def insert(self,tile,author,year,no):
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(tile,author,year,no))
        self.conn.commit ()


    def view(self):
        self.cur.execute("SELECT * FROM book")
        row = self.cur.fetchall()
        return row

    def search(self,title="",author="",year="",no=""):
        self.cur.execute ("SELECT * FROM book WHERE title = ? OR author = ? or year = ? OR no =?",(title,author,year,no))
        row = self.cur.fetchall()
        return row

    def delete(self,id):
        self.cur.execute ("DELETE FROM book WHERE id =?", (id,))
        self.conn.commit ()


    def update(self,id,title,author,year,no):
        self.cur.execute ("UPDATE book SET title =?,author = ?,year = ? ,no =? WHERE id=?", (title, author,year,no,id))
        self.conn.commit ()

    def __del__(self):
        self.conn.close()




#nsert("The sun","will","1992","1000001")
#delete(2)
#update(4,"the moon","smooth",1993,19992020)
#print(view())
#print(search(author="jhon smith"))