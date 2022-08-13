import eel
eel.init('user')
state = ' '


@eel.expose
def sendstate(stateparam):
    print("change in state"+ " state is " + stateparam)
    global state
    state = stateparam
    eel.switchpage(state)




eel.start('useraccess.html' , port=8080)
