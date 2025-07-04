import random
import string

len=int(input("Enter length of password: "))
password=""
print("Enter 1 to add character in password\nEnter 2 to add digits in password\nEnter 3 to add special charaters in password\nEnter 4 to exit\n")
while(True):
    c=input("Pick a number: ")

    if c=='1':
        password+=string.ascii_letters

    elif c=='2':
        password+=string.digits
        
    elif c=='3':
        password+=string.punctuation
        
    elif c=='4':
        if(password==""):
              print("First select char set")
        else:
            break
    else:
        print("Enter valid input!!!")

pw=""

for i in range(len):
    pw+=(random.choice(password))
print(f"Password generated is",pw)
