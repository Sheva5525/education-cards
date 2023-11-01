import sqlite3
      
class bd_user() :
    def __init__(self, name_file, name_table):
        self.name_table = name_table
        self.name_file = name_file
        self.conn = sqlite3.connect(name_file)
        self.cur = self.conn.cursor()
        try:
            str_crate = "CREATE TABLE " + name_table + " (id INTEGER, login TEXT, password TEXT);"
            self.cur.execute(str_crate)
            self.conn.commit()
        except sqlite3.OperationalError:
            pass
        return 
    
    def add_user(self, id_user, login, password):
        if  self.get_user(login) :
            str_crete = "INSERT INTO " + self.name_table + " (id, login, password) VALUES (?, ?, ?);"
            self.cur.execute(str_crete, (id_user, login, password))
            self.conn.commit()
            print("Add yser", login)
            return True
        return False

    def get_user(self, login):
        str_crete = "SELECT * FROM " + self.name_table + " WHERE LOGIN=?;"
        self.cur.execute(str_crete, (login,))        
        x = self.cur.fetchall()
        print(x)
        return len(x) == 0 


