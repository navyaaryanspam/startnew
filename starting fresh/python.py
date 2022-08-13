import mysql.connector
import eel
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Nav@12905')
mycursor = mydb.cursor()
eel.init('user')
state =  ' '
def create_database(dbname):
    mycursor.execute(("create database if not exists {}").format(dbname))
    mycursor.execute (('USE{}').format(dbname))
    print ('db created and now in use')

def create_table(tablename , dataformat):
    mycursor.execute(("create table if not exists {}({})").format(tablename,dataformat))
    print ('created table ', tablename)

@eel.expose
def sendstate(stateparam):
    print("change in state"+ " state is " + stateparam)
    global state
    state = stateparam
    statechangereact(stateparam)
    eel.switchpage(stateparam)
def statechangereact (stateparam):
    if (stateparam == 'loginpage'):
        create_database ('THE_LAST_CHAPTER')
        
        
eel.start('useraccess.html')


