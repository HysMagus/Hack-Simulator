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
        break
    else:
        io("Invalid user/password!\n")
