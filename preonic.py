def main():
    cmd = raw_input('''Possible commands: 
    l - print keyboard layout
    s - common shortcuts that you keep forgetting
    m - randomly generated motivational message
    ----------------------------------------
    Please enter a command:
    >>> ''')
    type(cmd)
    
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
    
# -----------------------

if __name__ == "__main__":
    main()
