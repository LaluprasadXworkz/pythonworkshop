class Application:

    def __init__(self,application_name,catogary,company,app_size,no_of_users,ratings):
        self.application_name=application_name
        self.catogary=catogary
        self.company=company
        self.app_size=app_size
        self.no_of_users=no_of_users
        self.ratings=ratings


    def sigup(self):
        print(f"Sigup done ,{self.application_name}")

    def login(self):
        print(f"Welcome to {self.application_name}")

    def logout(self):
        print("Thank You for using")

    def info(self):
        print()




app1=Application("Instagram","social Media",
                 "meta",42.47,1000,4.4)

app2=Application("Facebook","social Media","meta",
                 100,10000000,4.8)

app3=Application("whatsapp","social Media","meta",
                 46.40,5700000,7.3)

app1.sigup()
app1.login()
app1.logout()