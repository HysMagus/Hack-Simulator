import time

def io(i):
    for c in i:
        time.sleep(.1)
        print(c,end="",flush=True)

io("Initializing...\n")
while True:
    io("login: ")
    usr = input()
    io("password: ")
    pwd = input()

    if usr == "root" and pwd == "supervisor":
        io("Welcome back!\n")
        io("Terminal: " )
        TermInp = input()
        if TermInp == "ls" or TermInp == "help()":          
            io("E:/ , Documents, Downloads, Pictures, P0rn")
            io("Terminal:\n")
            TerminalInp1 = input()
            if TerminalInp1 == "cd E:/":
                    io("ERROR USB is PASSWORD PROTECTED USE E:/ -pass:PASSWORD to access")
            if TerminalInp1 == "Documents":
                    io("Taco.txt")
            if TerminalInp1 == "Downloads":
                    io("SherlockS1E1P1")
            if TerminalInp1 == "Pictures":
                    io("Folder is Emptry")
            if TerminalInp1 == "Git":
                    io("Insufficient privileges, please run as root")            
        break
    else:
        io("Invalid user/password!\n")
