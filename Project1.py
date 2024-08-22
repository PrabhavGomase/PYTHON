#PROGRAM 1
#AUTOMATED VENDING MACHINE SIMULATION
print("TYPE 1 TO SELECT ITEM A (Price $2) \nTYPE 2 TO SELECT ITEM B (Price $3) \nTYPE 3 TO SELECT ITEM C (Price $5")
can=False
while True:
    # not using int(input) as otherwise item would throw error when Cancel Transaction is entered
    if can:
        break
    item = input("Select Item: ")
    if item == "Cancel Transaction":
        print("Transaction cancelled")
        #Exiting
        break
    else:
        match (int(item)):
            case 1:
                # creating s to store sum of amounts entered
                s = 0
                A = input("Insert : ")
                # Cancel Transactionting
                if A == "Cancel Transaction":
                    print("Transaction cancelled")
                    print("")
                    break
                else:
                    # executes this code only if not Cancel Transactionted
                    a = int(A)
                    # adding the amount inserted into total amount inserted till now
                    s += a
                    # loop runs till total amount is enough to buy item A or user Cancel Transactions
                    while s < 2:
                        A = input("Insufficient amount. Insert : ")
                        if A == "Cancel Transaction":
                            print("Transaction cancelled")
                            can=True
                            break
                        else:
                            a = int(A)
                            s += a
                # not printing this if user Cancel Transactions
                    if A != "Cancel Transaction":

                        print("Dispensing item A. your change is : ", s - 2)
            case 2:
                s = 0
                A = input("Insert : ")
                if A == "Cancel Transaction":
                    print("Transaction cancelled")
                    can=True
                    break
                else:
                    a = int(A)
                    s += a
                    while s < 3:
                        A = input("insufficient amount. Insert : ")
                        if A == "Cancel Transaction":
                            print("Transaction cancelled")
                            can=True

                            break
                        else:
                            a = int(A)
                            s += a
                    if A != "Cancel Transaction":

                        print("Dispensing item B. your change is : ", s - 3)
            case 3:
                s = 0
                A = input("Insert : ")
                if A == "Cancel Transaction":
                    print("Transaction cancelled")
                    break
                else:
                    a = int(A)
                    s += a
                    while s < 5:
                        A = input("Insufficient amount. Insert : ")
                        if A == "Cancel Transaction":
                            print("Transaction Cancelled")
                            can=True
                            break
                        else:
                            a = int(A)
                            s += a
                    if A != "Cancel Transaction":
                        print("Dispensing item C. your change is : ", s - 5)
#PROGRAM 2
#SIMPLE ATM MACHINE
balance=500
print("TYPE 1 TO CHECK BALANCE \nTYPE 2 TO WITHDRAW MONEY \nTYPE 3 TO DEPOSIT MONEY \nTYPE 4 TO EXIT ")
while True:
    #Implemented while loop
    # taking input
    x=int(input("Enter: "))
    # using math case as more efficient to if elif loops 
    match(x):
        case 1:
            print("Your current balance is: ",balance)
        case 2:
            # taking amount to be withdrawn
            y=int(input("Enter: "))
            if(y>500):
                print("Insufficient funds.Please enter  a lesser amount")
            else:
                #subtracting from balance
                balance-=y
                print(y,"has been withdrawn.Your new balance is ",balance)
        case 3:
            z=int(input("Enter: "))
            #adding the amount inserted to the acount
            balance+=z
            print(z,"has been deposited.Your new balance is ",balance)
        case 4:
            print("Thank Your for Using the ATM.GoodBye!")
            break



