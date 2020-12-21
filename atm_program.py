import function
from atm_card import ATMCard
from customer import Customer
 

id = 0
condition = 1
cardNumber = ""
cardPIN = 0
cardBalance = 0
cardDetail = []
customer1 = Customer(id, cardPIN, cardBalance)

while condition == 1:

    input = function.showFirstMenu()
       
    if(input >= 0 and input <= 2):
        if input == 1:
            cardDetail = function.optionOneFirstMenu()
            #card = [cardNumber, cardPIN, cardBalance]
            
            id += 1  
            
            card1 = ATMCard(cardDetail[1], cardDetail[2])
            customer1 = Customer(id, cardDetail[1], cardDetail[2])

        elif input == 2:
            result = function.optionTwoFirstMenu(id, cardDetail)

            while(result == True):
                    input2 = function.showSecondMenu()

                    if input2 == 1:
                        function.printCustPIN(customer1.getCustPin())
                    elif input2 == 2:
                        result2 = function.changeCustPIN(customer1.getCustPin())
                        if(result2 != False):
                            customer1.changeNewPin(result2)
                    elif input2 == 3:
                        function.printCustBalance(customer1.getCustBalance())
                    elif input2 == 4:
                        wtdMoney = function.withdrawMoney()
                        if wtdMoney <= customer1.getCustBalance():
                            print(str(wtdMoney) + " has been withdrawn from your account")
                            wtdResult = customer1.withdraw(wtdMoney)
                            print("Your Balance: " + str(wtdResult))
                        else:
                            print("Sorry your balance is not enough to be withdrawn")
                    elif input2 == 5:
                        dptMoney = function.depositMoney()
                        print(str(dptMoney) + " has been deposited to your account")
                        dptResult = customer1.deposit(dptMoney)
                        print("Your Balance: " + str(dptResult))
                    elif input2 == 6:
                        function.exitSecondMenu(customer1.getCustBalance())
                    else:
                        print("Not available, you must input from 1-6. Please try again!!")

        else: 
            condition = 0
            exit()
    else:
        print("Not available, you must input from 0-2. Please try again!!")    