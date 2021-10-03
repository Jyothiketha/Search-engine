import psycopg2

connection= psycopg2.connect(
    database= "searchengine",
    user="postgres",
    password="Sarvaani@8",
    host="localhost",
    port="5432")
#print(connection)
hostman=connection.cursor()

def create_searchhistory():
    hostman.execute('''CREATE TABLE SearchHistory(
     ID SERIAL PRIMARY KEY NOT NULL,
     FILENAME varchar NOT NULL,
     FILE_EXTENSION varchar NOT NULL,
     LOCATION varchar NOT NULL''')
    connection.commit()
    print("Table is created")
    connection.close()

def insert_searchhistory():
    hostman.execute('''INSERT into SearchHistory(FILENAME,FILE_EXTENSION,LOCATION) 
                            VALUES('manage','.py','D:\Zensar\python project\manage.py')''')
    connection.commit()
    print("record is created")
    connection.close()

def searchhistory():
    hostman.execute('''SELECT FROM SearchHistory where FILENAME=filename''')
    connection.commit()
    print("searching is created")
    connection.close()

def select_searchhistory():
    hostman.execute('''select * from SearchHistory''')
    connection.commit()
    selectrows = hostman.fetchall()
    for each_row in selectrows:
        print(each_row)

def count_searchhistory():
    count_sql_searchhistory='''SELECT FILENAME,FILE_EXTENSION,LOCATION ,count(*) from SearchHistory
                               group by FILENAME,FILE_EXTENSION,LOCATION HAVING count(*) > 1'''
    hostman = connection.cursor()
    hostman.execute(count_sql_searchhistory)
    connection.commit()
    print("records are counted")
    connection.close()

insert_searchhistory()

