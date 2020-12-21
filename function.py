import datetime
import random

def wrongInputPIN():
    print("You have inputed your PIN wrongly until three times.")
    print("Please take your card and try again!!")
    exit()

def showFirstMenu():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    
    return int(input(' ')) 

def optionOneFirstMenu():
    cardNumber = str(random.randint(10000000,40000000)) + str(random.randint(61234567,99999999))
    cardPIN = 123456 
    cardBalance = 10000
    print("Your card has been created")
    print("Your card number:")
    print(cardNumber)
    print("Your card PIN:")           
    print(cardPIN)

    card = [cardNumber, cardPIN, cardBalance]
    return card

def optionTwoFirstMenu(id, card):
    trialCN = 0
    trialPN = 0
    check = False

    while id > 0 and trialCN < 3:
        print("Enter your card number:")
        inputCardNumber = input(' ')

        if inputCardNumber == card[0]:
            while trialPN < 3:
                print("Enter your PIN (6 numbers):")
                inputCardPIN = int(input(' '))
               
                if inputCardPIN == card[1]:
                    check = True
                    return check
                else:
                    print('You have inputed wrong PIN. Please try again!')
                    check = False
                    trialPN += 1
        else:
            print('You have inputed wrong card number. Please try again!')
            check = False
            trialCN += 1      
        
        if(trialPN >= 3 or trialCN >= 3):
            print("You have inputed wrongly until three times. Please take your card and try again!!")
            exit()
        
    print("You haven't yet had an account. Please create it first!!")
    return check

def showSecondMenu():
   
    print("You have successfully logged in!")
    print("1. Check PIN")
    print("2. Change PIN")
    print("3. Check Balance")
    print("4. Withdraw Money")
    print("5. Deposit Money")
    print("6. Exit")
    
    return int(input(' '))

def printCustPIN(custPIN):
    print("Your PIN:")
    print(custPIN)

def changeCustPIN(custPIN):
    inputNewPIN = 0
    trial = 0
    while trial < 3:
        print("Input your old PIN:")
        inputOldPIN = int(input(' '))
        
        if inputOldPIN == custPIN :
            break
        else:
            print("Your PIN has been inputed wrongly!")
            trial += 1
            continue

    if trial >=3:
        wrongInputPIN()
    else:
        trial1 = 0
        while trial1 < 3:
            print("Input your NEW PIN (6 numbers):")
            inputNewPIN = input(' ')
            if len(inputNewPIN) == 6:
                print("Your PIN have been changed successfully..")
                break
            else:
                print("Your pin must use 6 numbers. Try to input again!!")
                trial1 += 1
            
        if trial1 >= 3:
            wrongInputPIN()
            return False
               
    return inputNewPIN                  

def printCustBalance(custBalance):
    print("Your Balance:")
    print(custBalance)


def withdrawMoney():
    print("Input how much money do you want to withdraw:")
    return int(input(' '))
    
def depositMoney():
    print("Input how much money do you want to deposit:")
    return int(input(' '))
       

def exitSecondMenu(custBalance):
    noRecord = random.randint(100000, 1000000)
    print("Record No: " + str(noRecord))
    dateTime = str(datetime.date.today()) + ' ' + str(datetime.datetime.now())
    print(dateTime)
    print("Your last balance: " + str(custBalance))                        
    exit()
