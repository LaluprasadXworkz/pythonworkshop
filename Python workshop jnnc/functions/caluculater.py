def userInput():
    first_input=int(input("Enter the First Number  :"))
    second_input=int(input("Enter the Second Number :"))
    return  first_input,second_input


def add(a=0,b=0):
    return a+b

def sub(a=0,b=0):
    return  a-b

def mult(a=0,b=0):
    return  a*b

print("Wellcome to cal")
while True:
    print("Select the choose :\n 1:Add \n 2:sub \n 3:mult \n 4:stop ")
    choose=int(input("Enter the choose :"))

    if choose==1:
        x,y=userInput()
        print(f"Addition of two Number : {add(x,y)}")

    elif choose==2 :
        x,y=userInput()
        print(f"Sub of two Number : {sub(x,y)}")

    elif choose==3:
        x,y=userInput()
        print(f"Multiplication of two Number :{mult(x,y)}")

    elif choose==4:
        print("Thank you for Using  calculate")
        break