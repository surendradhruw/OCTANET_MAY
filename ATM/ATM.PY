print("\n\nWelcome to SBI Bank:\n")
password=9770
choice=0
balance=10000
pin=int(input("Enter your PIN number :\n"))
if pin==password:
    while choice!=4:
        print("\n------------------**Menu**----------------------\n")
        print("1--> withdraw.")
        print("2--> check balance.")
        print("3--> Deposit.")
        print("4--> cancle.")
        print("----------------------***--------------------------")

        choice=int(input("\n<-:Enter your option:->\n"))
        if choice==2:
            print("\nYour current balance is-->",balance)
        elif choice==1:
             wit=int(input("Enter your withdrwal amount::"))
             balance-=wit
             print("\nYour current balance is::",balance)
             print("\twithdrawal amount::",wit)
        elif choice==3:
             dep=int(input("Enter your deposit amount:"))
             balance+=dep
             print("\n\nCurrent balance is::",balance)
             print("\tDeposit amount is ::",dep)
        elif choice==4:
             print("\n\n Sesson Ended : ")

else:
        print("Invailid PIN. Try again :")


      


 
    



        
        