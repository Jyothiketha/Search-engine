import psycopg2

connection= psycopg2.connect(
    database= "searchengine",
    user="postgres",
    password="Sarvaani@8",
    host="localhost",
    port="5432")
# print(connection)
hostman = connection.cursor()

def create_register():
    hostman.execute('''CREATE TABLE Registration (
    ID SERIAL PRIMARY KEY NOT NULL,
    USERNAME varchar NOT NULL,
    EMAIL varchar NOT NULL,
    PASSWORD varchar NOT NULL,
    CONFIRM_PASSWORD varchar NOT NULL)''')
    connection.commit()
    print("Table is created")
    connection.close()

def insert_register():
    hostman.execute('''INSERT into Registration(USERNAME,EMAIL,PASSWORD,CONFIRM_PASSWORD) VALUES (%s,%s,%s,%s)''',(Username,Email,Password1,Password2) )
    connection.commit()
    print("record is created")
    connection.close()

def create_login():
    hostman.execute('''CREATE TABLE Login (
    ID SERIAL PRIMARY KEY NOT NULL,
    USERNAME varchar NOT NULL,
    PASSWORD varchar NOT NULL)''')
    connection.commit()
    print("Table is created")
    connection.close()

def insert_login():
    hostman.execute('''insert into Login(USERNAME,PASSWORD) VALUES (%s,%s)''',(Username,Email,Password1) )
    connection.commit()
    print("record is created")
    connection.close()


def create_query():
    hostman.execute('''CREATE TABLE SearchEngine(
     ID SERIAL PRIMARY KEY NOT NULL,
     FILENAME varchar NOT NULL,
     LOCATION varchar NOT NULL)''')
    connection.commit()
    print("Table is created")
    connection.close()

def insert_query():
    hostman.execute('''INSERT into SearchEngine(FILENAME,LOCATION) VALUES(%s,%s)''',(filename,result))
    connection.commit()
    print("record is created")
    connection.close()

























jyothi, Sarvaani@8, Sarvaani@8
