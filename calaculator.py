c='y'
while c=='y':
    try:
            a=int(input("Enter 1st number: "))
            b=int(input("Enter 2nd number: "))
            op=input("Enter operation to be performed(+,-,*,/): ")
            match op:
                case '+':
                    print(f"The result is ",a+b)
                case '-':
                    print(f"The result is ",a-b)
                case '*':    
                    print(f"The result is ",a*b)
                case '/':
                    print(f"The result is ",a/b)
                case default:
                    print("Invalid operation!!!")

    except Exception as e:
        print("Error occured!",e)

    c=input("Do you want to continue?(y/n): ")