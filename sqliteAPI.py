import sqlite3

class SQL_option():

    def __init__(self,db:str):
        self.db_name = db
        self.db = sqlite3.connect(db)
        print(f"数据库{db}连接成功")
    
    def create_new_table(self,name:str)->bool:
        
        c = self.db.cursor()

        c.execute(f'''CREATE TABLE {name}
                    (TIME INT PRIMARY KEY NOT NULL,
                     DATA TEXT             NOT NULL);''')
        self.db.commit()
        c.close()
        print(f"{name}表创建成功")
        return True

    def insert_to_table(self,data:list)->bool:

        c = self.db.cursor()
        for contain in data:
            sql_query = f"""INSERT INTO {contain['DEVICE']} (TIME,DATA)
                            VALUES ( {contain['TIME']}, {contain['DATA']} );"""
            c.execute(sql_query)
            print(f"数据插入{contain['DEVICE']}表成功")
        self.db.commit()
        c.close()
        
        return True

    def select_from_table(self,table:str):

        c = self.db.cursor()
        result = c.execute(f"SELECT TIME, DATA FROM {table} ORDER BY TIME DESC LIMIT 1;")
        for data in result:
            a = data[0]
            b = data[1]
        c.close()
        return a,b

    def clear_whole_table_contains(self,table:str)->bool:

        c = self.db.cursor()
        c.execute(f"DELETE FROM {table};")
        self.db.commit()
        c.close()
        print(f"清空{table}表内容成功")
        return True
    
    def is_table_exist(self,table:str)->bool:

        c = self.db.cursor()
        result = c.execute(f"SELECT count(*) from sqlite_master where name='{table}' and type='table'")
        
        for i in result:
            result = i[0]

        if result == 1:
            result = True
        else:
            result = False

        return result

    def delete_table(self,table:str):
        c = self.db.cursor()
        c.execute(f"DROP TABLE {table}")
        self.db.commit()
        c.close()
        print(f"删除{table}表")

    def close_db(self):
        self.db.close()
        print(f"关闭{self.db_name}数据库")

if __name__ == "__main__":
    data = [{"TIME":999,"DATA":999},{"TIME":1000,"DATA":154}]
    test = SQL_option("test.db")
    #print(test.select_from_table("S11"))
    #print(test.is_table_exist("test"))
    #test.clear_whole_table_contains("test")
    #test.create_new_table("test")
    #test.fun_insert("test",data)
    #test.delete_table("S31")