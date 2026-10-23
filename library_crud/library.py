import mysql.connector

class BookManager:
    def get_connect(self):
        try:
            self.connection=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Shehnasameer$1",
                database="library_db"
            )
            return self.connection
        except Exception as e:
            return  None

    def get(self):
        try:
            self.cursor=self.connection.cursor()
            query="select * from book"
            self.cursor.execute(query)
            record=self.cursor.fetchall()
            return record
        except Exception as e:
            print(e)
    def get_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from book where id=%s"
            value=[id,]
            self.cursor.execute(query,value)
            record=self.cursor.fetchone()
            return  record
        except Exception as e:
            return None
    def retrive(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from book where id=%s"
            value=[id,]
            self.cursor.execute(query,value)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)
    def post(self,**kwargs):
        try:
            self.cursor=self.connection.cursor()
            query=""" insert into book(title,author,catagory,price,publishes_year) values(%s,%s,%s,%s,%s)"""
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("book published success")
        except Exception as e:
            print(e)
    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record !=None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k +"=%s,"
                    placeholder=placeholder.rstrip(",")
                    query=f"update book set{placeholder}where id=%s"
                    values=[v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query,values)
                    self.connection.commit()
                    print("book table updated")
            else:
                print("book not found")
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            record=self.get_object(id=id)
            value=[id,]
            if record!=None:
                query="select * from book where id=%s"
                self.cursor.execute(query,value)
                self.connection.commit()
                print("data delete success")
            else:
                print("record not found")
        except Exception as e:
            print(e)
connect_instance=BookManager()
print(connect_instance.get_connect())
connect_instance.get()
#connect_instance.post(title=" note book",author="arshit",catagory="novel",price=100,publishes_year="2024")
#connect_instance.post(title=" note book1",author="manu",catagory="novel",price=100,publishes_year="2024")
#connect_instance.post(title=" note book2",author="akash",catagory="novel",price=100,publishes_year="2025")
#connect_instance.get()
connect_instance.retrive(3)
connect_instance.put(4,price=200)