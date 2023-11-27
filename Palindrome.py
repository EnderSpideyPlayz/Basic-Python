#Get The Word As An Input From The User.
my_string = input("Enter a String : ")

#Change The Input String To Lower Case.
my_string_lower = my_string.lower()

#Find The Length Of The String.
len_string = len(my_string_lower)

#Set Indexes To Check Extract Each Letter Of The String.
i = 0
j=len_string - 1

#Check If The Letters In The Word Are Same Or Not When The Word Is Reversed.
for i in range(len_string):

#Set The Flag To First If The First And Last Index Letters Are The Same.
    if(my_string_lower[i] == my_string_lower[j]):

        i = i + 1
        j = j - 1
        flag = 1

    else:
        flag = 0
        break

if(flag == 1):
    print("It's A Palindrome")

if(flag == 0):
    print("It's Not A Palindrome")