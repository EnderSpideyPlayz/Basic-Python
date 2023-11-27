check_another = "yes"
while check_another == "yes":
    my_string = input("Enter your string:- ")
    my_string=my_string.lower()
    rev_string = ""
    for char in my_string:
        rev_string = char + rev_string
    if (my_string == rev_string):
        print("Yes, it's a palindrome")
    else:
        print("No, it's not a palindrome")
    check_another = input("Please enter yes if you want to check another word? ")