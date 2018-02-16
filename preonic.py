def main():
    cmd = raw_input('''Possible commands: 
    l - print keyboard layout
    s - common shortcuts that you keep forgetting
    m - randomly generated motivational message
    f - freeze google inspector 
    ----------------------------------------
    Please enter a command:
    >>> ''')
    type(cmd)
    
    if (cmd == 'l'):
        layout()
        main()
    elif (cmd == 's'):
        shortcuts()
        main()
    elif (cmd == 'm'):
        randomMessage()
        main()
    elif (cmd == 'f'):
        freeze()
        main()
    elif (cmd == 'q'):
        quit()
    else:
        main()
    
#     choices = {
#         'l': layout(),
#         'm': randomMessage() 
#         }
#     result = choices.get(cmd, "wrong")
    
def layout():
    layout = '''Preonic Qwerty Layout
    |   `  |   1  |   2  |   3  |   4  |   5  |   6  |   7  |   8  |   9  |   0  | Bksp |  
    |------+------+------+------+------+------+------+------+------+------+------+------|  
    | Tab  |   Q  |   W  |   E  |   R  |   T  |   Y  |   U  |   I  |   O  |   P  | Del  | 
    |------+------+------+------+------+-------------+------+------+------+------+------| 
    | Esc  |   A  |   S  |   D  |   F  |   G  |   H  |   J  |   K  |   L  |   ;  |  \   | 
    |------+------+------+------+------+------|------+------+------+------+------+------| 
    | Shift|   Z  |   X  |   C  |   V  |   B  |   N  |   M  |   ,  |   .  |   /  |Enter | 
    |------+------+------+------+------+------+------+------+------+------+------+------| 
    | Brite| Ctrl | Alt  | GUI  |Lower |    Space    |Raise | Left | Down |  Up  |Right |
    .-----------------------------------------------------------------------------------.
    
    '''
    print layout
    
def randomMessage():
    randomMessage = "c's get degrees"
    print randomMessage

def shortcuts():
    print ("Run code (eclipse): CTRL + LOWER + B // CTRL + F11")
    
def freeze():
    freeze = '''
    setTimeout(function(){debugger;}, 5000)
    '''
    print freeze

# -----------------------

if __name__ == "__main__":
    main()
