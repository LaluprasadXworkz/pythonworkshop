user_name=input("Enter the username : ")
if(user_name=="user"):
    print("UserName is valid")
    password=input("Enter password : ")
    if(password=="user@123"):
        print("Login Successfull")
    else:
        print("Login un successfull")
else:

    print("UserName is not valid")