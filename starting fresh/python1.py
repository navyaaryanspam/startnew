import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Nav@12905')
mycursor = mydb.cursor()
def create_database():
    mycursor.execute("create database if not exists THE_LAST_CHAPTER")
create_database()

mycursor.execute ('USE the_last_chapter')
# admin book inventory
try:
    mycursor.execute("create table  trial1 (book_id int(5) primary key,book_name varchar(20), book_pic varbinary (max), author_name varchar(20),genre_name varchar(20),price int(5),ratings int(5))")
    print ('table made')

except :
    print ('table already exists')


