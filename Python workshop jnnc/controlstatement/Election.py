Age = int(input("Enter ur age"))
def vote(Age):
    if(Age>18):
        print("Eligible to vote")
    elif(Age<18):
        print("Not eligible")

vote(Age)
