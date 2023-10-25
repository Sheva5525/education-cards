import sqlite3

class reques_bd:
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cur = self.conn.cursor()
    
    def exec_commit(self, string, parameters = ()):
        self.cur.execute(string, parameters)
        self.conn.commit()

    def select(self, name, value = NULL id_value = None)->int:
        str_select = "SELECT {} FROM {};".format(id_value if ( id_value ) else "*", name)
        self.exec_commit(str_select)
    
    def insert(self, name, value):
        str_insert = "INSERT INTO {} VALUES{};".format(name, reques_bd.creat_value(len(value)))
        self.exec_commit(str_insert, value)

    def creat_table(self, name, parameters):
        str_crate = "CREATE TABLE " + name + "(" + parameters + ");"
        self.exec_commit(str_crate)

    def creat_value(len_value):
       return "(" + ("?, " * len_value)[:-2] + ")"
        
        
        
    
class bd_user(reques_bd):
     def __init__(self, name, name_table = "USERS"):
         super().__init__(name)
         self.name_table = name_table
         str_atribut = "ID INTEGER, LOGIN TEXT, PASSWORD TEXT"
         self.creat_table(self.name_table, str_atribut)

     def add_key(self, id_user, login, password):
         self.insert(self.name_table, (id_user, login, password)) 
