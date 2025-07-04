import random
un=input("Enter your name:")
conti='y'
while conti=='y':
    print("Enter--> \n1 for Rock\n2 for Paper\n3 for Scissor")
    user=input("Your turn: ")
    if user=='1':
        print(f"{un}'s choice is Rock")
    elif user=='2':
        print(f"{un}'s choice is Paper")
    elif user=='3':
        print(f"{un}'s choice is Scissor")
    else:
        print("Enter valid input")
        break
    print("Now computers turn....")
    cc="123"
    comp=""
    for i in range(1):
        comp=random.choice(cc)
    
    if comp=='1':
        print("Computer's choice is Rock")
    elif comp=='2':
        print("Computer's choice is Paper")
    elif comp=='3':
        print("Computer's choice is Scissor")
    final=""
    
    if(user==1 and comp==3) or (user==3 and comp==1):
        final='1'
    elif(user==2 and comp==1) or (user==1 and comp==2):
        final='2'
    elif(user==3 and comp==2)or (user==2 and comp==3):
        final='3'

    if user==comp:
        print("Its a draw!")
    elif final==user:
        print("{un} wins!!!")
    else:
        print("Computer wins!!!")

    conti=input("Do you want to continue?(y/n): ")
