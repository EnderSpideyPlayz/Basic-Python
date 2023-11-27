# import random  # print(10+20)
# print(10-20)
# print(10*20)
# print(10/20)
# print(10//20)
# print(10%3)
# print(10**3)

# x=10
# y=20
# print(not x==10 and x<y)

# print(5>2)

# a=10
# b=20
# print("This is an identity operator", a is b)

# l = [10,20,30,40,50]
# print(102 in l)
# a=30
# b=20
# print(bin(a), bin(b))
# print(a&b)
# print(a^b, bin(a^b))
# l=[10,20,30,"hello"]
# l[0] = 5
# l[3] = "welcome"
# print(l)
# print(type(l))
# a=(10)
# print(a, type(a))
# s = '''rock
# paper
# scissors'''
# print(s)
#t = (10,20,30,40,50)
# print(t, type(t))
# l = [10,20,30,40,50]
# print(l, type(l))
# d = {
#     "course_name":"Python",
#     "fees":12000,
#     "duration":"2 Months"
# }
# d["fees"] = 10000
# print(d, type(d))
# s = {10,20,30,50,40}
# s[0] = 10
# print(s, type(s))
# a=eval(input("Enter First Number"))
# b=eval(input("Enter Second Number"))
# print(a+b)
# a=int(input("Enter Marks"))
# if a > 80 and a<=100:
#     print("A")
# elif a<=80 and a>=60:
#     print("B")
# elif a<=60 and a>=40:
#     print("C")
# else:
#     print("fail")
# a = int(input("Enter Number"))
# if a % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# a = (input("Enter Your Color"))
# if a == "green" or a == "Green":
#     print("Go")
# elif a == "yellow" or a =="Yellow":
#     print("Wait")
# elif a == "red" or a == "Red":
#     print("Stop")
# else:
#     print("Invaid Input")
#a = int(input("Enter No."))
#if a < 0:
#    print("It is negative")
#elif a > 0:
#     print("It is positive")
# else:
#     print("The number is zero")
#Order
# print(ord("@"))
#CHR
# print(chr(64))
#For Loop-->Self Increment Loop, Range --> (Starting Post, Condition, Increment)
# for a in range(20,-1,-2):
#     print(a)
# a = [10,20,30]
# t = len(a)
# for b in range(t):
#    print(a[b])
# for a in range(1,5):
#    print(a)
# for i in range(10,-1,-1):
#    print(i)
# While loop:
# i = 10
# while i>=0:
#    print(i)
#    i=i-1
# #Star Pattern
# for i in range(1,6):
#    for j in range(1,6-i+1):
#       print("*", end="")
#    print("")
#String Indexing And Slicing:
# s = "hello to python class"
# print(s[0], s[6])
# s="hello to python class"
# print(s[-1:-6:-1])
#String Iteration
# s="hello to python class"
# t = len(s)
# for a in range(t):
#    print(s[a])
#s = "hello to python class"
# t= len(s)
# for a in range(t-1,-1,-1):
#    print(s[a])
# s = "hello to python class"
# s = "hello to python class"
# print(s.capitalize())
# print(s.title())
# print(s.upper())
# s = "hello to python class"
# print(s.find("c"))
# s = "hellotopythoncslass123"
# print(s.isdigit())
# print(s.isalpha())
# print(s.isalnum())


#Calculator
# print('''
# + Add
# - Subtract
# * Multiply
# / Divide
# // Floor Divide
# % Modulus
# ** Exponent
# ''')
# num1 = int(input("Enter First No."))
# num2 = int(input("Enter Second No."))
# opr = input("Enter Operator")
# if opr=='+' :
#     print(num1+num2)
# elif opr=='-':
#     print(num1-num2)
# elif opr=='*' :
#     print(num1*num2)
# elif opr=='/' :
#     print(num1/num2)
# elif opr=='//' :
#     print(num1//num2)
# elif opr=='%':
#     print(num1%num2)
# elif opr=='**':
#     print(num1%num2)
# else:
#     print('Invalid Input')
#
# if opr=='+' :
#     print(num1+num2)
# if opr=='-':
#     print(num1-num2)
# if opr=='*' :
#     print(num1*num2)
# if opr=='/' :
#     print(num1/num2)
# if opr=='//' :
#     print(num1//num2)
# if opr=='%':
#     print(num1%num2)
# if opr=='**':
#     print(num1%num2)
# if opr!='+' and opr!='-' and opr!='*' and opr!='/' and opr!='//' and opr!='%' and opr!='**':
#     print('Invalid Input')
#
# Patterns
# k=1
# for i in range(1,6):
#     for j in range(1,6-i+1):
#         print(k," ",end="")
#         k=k+1
#     print("")
# String Format
# s="welcome {} to {} python class".format("hello", "20")

# print(s)
# x = int(input("Enter Bank Balance"))
# s="You have {a:10} Rupees in your bank account".format(a=x)
# print(s)
# s="welcome {a:>20} python class".format(a="hello")
# print(s)
# CENTER ALIGN = ^, LEFT ALIGN = DEFAULT = <, RIGHT ALIGN = >
# l = [10,20,30,40,40]
# l[0] = 50
# print(l[3])

# LIST SLICING
# l = [10,20,30,40,50,60]
# # print(l[-1::-2])
# l = [10,20,30,40,50]
# for a in [l]:
#     print(a)
# t=len(l)
# for a in range(t):
#     print(l[a])
# s=[10,20,30,40,50]
# t = len(s)
# for a in range(t-1,-1,-1):
#     print(s[a])
# l = [10,20,30,40,50]
# l.clear()
# print(l)
#
# # 03/07/2023
# l = [10,20,30,40,50]
# l.insert(5,60)
# print(l)
#
#  Append
#  l = [5,10,15]
#  l.append(20)
# print(l)
#
# l = []
# for a in range(1,21):
#     l.append(a)
#     print(l)
#
# l = [10,20,30,40]
# x = [50,60,70,80]
# l.extend(x)
# print(l)
#
# List Comprehension
# for a in range(1,101):
#     print(a)
# l=[b for b in range(1,101) if b%2 ==0]
# print(l)
# s='hello'
# a = [b for b in s]
# print(a)

# a=[print("") or print("*",end="") for i in range(1,5) for j in range(1,i+1)]
# print(a)

# l = [10,20,30,40,20,20,20,20]
# print(l.count(20))
#l = [10,20,30,40,50,60,60]
#a=max(l)
# print(a)
# b=min(l)
# print(b)
# l = [10,20,30,40,50,60,30,20,10]
# l.sort()
# print(l)
# l = [10,20,30,40,50,60,60]
# print(l.index(40))
# l = [10,20,30,40,50]
# n = [16,70,80,90,100]
# for a,b in zip(l,n):
#     print(a,b)
# l = [10,20,30,40]
# n = [50,60,70,80]
# t = len(l)
# for a in range(t):
#      print(l[a], n[a])
#  s=(input("Enter String"))
#  s.split()
#  print(s)
#
# a=[[print("")] or print("*",end="") for j in range(1, i+1) for i in range(1,6)]
# Dictionary
# d={
#     "course name":"python",
#     "fees":"10000",
#     "course_duration":"1 month"
# }
# d["fees"]=20000
# print(d, type(d))
# d={
#      "course name":"python",
#      "fees":"10000",
#      "course_duration":"1 month"
#  }
# for i in d:
#      print(i)
#      print(d[i])
# d["fees"]="20000"

# d={
#      "course name":"python",
#      "fees":"10000",
#      "course_duration":"1 month"
#  }
# print(d.get("fees"))
# print(d.keys())
# print(d.items())
#x = d.items()
# for i in x:
#     print(i)
# a = dict('name' : 'Jack', 'age': v'8')
# d = {
#     "course_name":"python",
#     "fees":"12000",
#     "duration":"2m"
# }
# for a in d.values():
     # print(a)
# d.update({"fees":10000})
# print(d)
# Nested Dictionary
# d = {
#     'php':{"duration":"2months","fees":10000},
#     'java':{"duration":"3months", "fees":12000},
#     'python':{"duration":"4months", "fees":13000}
# }
# print(d,type(d))
# print(d['php'])
# print(d['php']["fees"])
# print(d.pop('php'), d)
# for a,b in d.items():
#     print(a,b)
# t = (10,20,30,40,50)
# l = len(t)
# for i in range(l):
#     print(t[i])
# t = (10,20,30,40,50)
# print(t,min(t))
# print(t,max(t))
# print(t,t.count(10))
# print(t,t.index(40))
# print(t,sum(t))
# e=str(input("Enter Your Email Id"))
# x=e[0]
# i=0
# l = len(e)
# if e.isspace():
#     print("Invalid ID")
#     if not x.isalpha():
#         print("Invalid ID")
#         if not l >= 6:
#             print("Invalid ID")
#             for i in range(e):
#                if not i == i.upper():
#                     print("Invalid ID")

# d={
#     "course_name":"python",
#     "fees":"10000 Rs",
#     "duration":"10 Months"
# }
# d["course_name"]="HTML"
# print(d,type(d))
# a=d.get("fees")
# print(a)
# for i,j in d.items():
#     print(i,j)
# q = dict(Name="Python", Fees="10000 Rs", Duration="10 Months")
# print(q.pop("Name"))
# q.update({"Fees":12000})
# print(q)

# NESTED DICTIONARY
#
# d = {
#     "python":{"Popular":2, "Rank":1},
#     "JS":{"Popular":1,"Rank":2},
# }
# print(d["JS"]["Rank"])
# for a,b in d.items():
#     print(a,b["Rank"])
# d["python"]["Rank"] = 2
# print(d["python"]["Rank"])

