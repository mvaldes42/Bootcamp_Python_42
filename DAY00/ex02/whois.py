import sys
if len(sys.argv) < 2:
    exit()
arg = sys.argv[1]
try:
    nbr = int(arg)
    if nbr == 0:
        print("I'm Zero.")
    elif (nbr % 2) == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except ValueError:
    print("ERROR")
