import sqlite3

class reques_bd:
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cur = self.conn.cursor()
    
    def exec_commit(self, string, parameters = ()):
        print(self.cur.execute(string, parameters).fetchone())
        self.conn.commit()

    def select(self, name, where = None, id_value = None)->int:
        str_select = "SELECT {} FROM {};".format(id_value if ( id_value ) else "*", name) 
        str_select += "WHERE " + where if where else ''
        self.exec_commit(str_select)
    
    def insert(self, name, value):
        str_insert = "INSERT INTO {} VALUES{};".format(name, reques_bd.creat_value(len(value)))
        self.exec_commit(str_insert, value)

    def creat_table(self, name, parameters):
        try:
            str_crate = "CREATE TABLE " + name + "(" + parameters + ");"
            self.exec_commit(str_crate)
        except sqlite3.OperationalError:
           pass
            
    def creat_value(len_value):
       return "(" + ("?, " * len_value)[:-2] + ")"
    
    def __del__(self):
        self.conn.close()
        
    
class bd_user(reques_bd):
     def __init__(self, name, name_table = "USERS"):
         super().__init__(name)
         self.name_table = name_table
         str_atribut = "ID INTEGER, LOGIN TEXT, PASSWORD TEXT"
         self.creat_table(self.name_table, str_atribut)

     def add_key(self, id_user, login, password):
         
         self.insert(self.name_table, (id_user, login, password))
