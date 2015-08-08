import time

def io(i):
    for c in i:
        time.sleep(.1)
        print(c,end="",flush=True)

io("Initializing...\n")
io("login: ")
usr = input()
io("password: ")
pwd = input()
