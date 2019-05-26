import sqlite3

class SQL_option():

    def __init__(self):
        self.db = sqlite3.connect("test.db")
    
    def createNewTable(self,name:str)->bool:
        
        c = self.db.cursor()

        c.execute(f'''CREATE TABLE {name}
                    (TIME INT PRIMARY KEY NOT NULL,
                     DATA 

                    )
                    ''')