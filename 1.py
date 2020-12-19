uname = str(input("enter your username "))
shtrodel = ("@" in uname)
dot = ("." in uname)
if (dot == 1) and (shtrodel == 1):
    pword = str(input("enter your password "))
    solamit = ("#" in pword)
    pword_len = len(pword)
    if solamit == 1 and pword_len >= 8:
        print("yeahhhhh boiiiii")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")
