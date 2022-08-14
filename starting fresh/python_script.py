import eel
eel.init('user')
state = ' '


@eel.expose
def sendstate(stateparam):
    print("change in state"+ " state is " + stateparam)
    global state
    state = stateparam
    eel.switchpage(state)

@eel.expose
def checklogin(usernameparam,passwordparam):
    print("login creds are username: " + usernameparam + " password: " + passwordparam)
    global username
    global password
    username = usernameparam
    password = passwordparam
    if (username == "admin" and password == "admin@123"):
        #admin
        eel.switchpage("adminwindow")

    else:
        #not admin
        eel.switchpage("errorpage")



eel.start('useraccess.html' , port=8080)
