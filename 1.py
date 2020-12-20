uname = str(input("Enter your username "))
shtrodel = ("@" in uname)
dot = ("." in uname)
if (dot == 1) and (shtrodel >= 1):
    pword = str(input("Enter your password "))
    solamit = ("#" in pword)
    pword_len = len(pword)
    if solamit == 1 and pword_len >= 8:
        print("Yeahhhhh Boiiiii")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")
