# I have chosen the following conditions:
# 1 "@" is mandatory
# No spaces are allowed
# First letter has to be an alphabet
# "." has to be present at either 3rd or 4th position from the right
# No capital letters
# Symbols other than ".", "_", "@" are not allowed
n = input("Enter your e-mail id ")
l = len(n)
k=0
j=0
d=0
if l > 5:
    if n[0].isalpha():
        if ("@" in n) and(n.count("@")==1):
            if(n[-4]==".") or (n[-3]=="."):
                for i in n:
                    if i==i.isspace:
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Invalid Email")
                else:
                     print("Correct Email")

            else:
               print("Invalid Email")
        else:
            print("Invalid Email")
    else:
        print("Invalid Email")
else:
    print(("Invalid Email"))