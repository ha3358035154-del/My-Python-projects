 # project number 1:- 
Appleprice = int(input("Plese Enter the today price of Apple:- "))
mybujet = 500
if mybujet - Appleprice>= 300:
    print("today rate is best please buy this mr.umair ")
elif mybujet - Appleprice>=200:
    print("please by half kg Apple you buject is low to buy otherthings")
elif mybujet - Appleprice>100:
     print("dont buy Apple your buject is very low ")
 else:
     print("please go to home you are very poor")

 # second mini project:
 num = int(input("Enter the value of num:- "))
 if num< 0:
     print("num is nejative")
 elif num>0:
     if num>0 and num<=10:
         print('num is lies between 0 and 10')
     elif num>10 and num<=15:
         print("num is lies between 10 and 15")
    elif num>15 and num<= 20:
      print("num is lies between 15 and 20")
    else:
       print("num is not find in 20numbers")
 else:
    print("you are out of the game you not follow the game rule")
 
#   Third project:
    
    student = input("You are a student of orbitfamily? (yes/no):")
if student == "yes":
     classno = int(input("Enter your class:"))
     if classno>= 9:
         print("you are allow for library ")
     else:
         print(" not Entery foryou  because are littleclass student")
else:
    print("you are not the orbit student")

# Forth project:-
studentname = input("Enter your name:-")
Math = int(input("Enter the maths marks:- "))
Englis = int(input("Enter the english marks:- "))
Physics = int(input("Enter the Physics marks:- "))
Urdu = int(input("Enter the urdu marks:- "))
obtainmarks = Math +Englis + Physics+ Urdu
Average = obtainmarks/5
print("Averagemarks is this",Average)
print("obtainmarks is this",obtainmarks)
if obtainmarks <50:
    print("you are fail")
else:
    print("pass")
if obtainmarks>= 90:
    print("A+")
elif obtainmarks>= 80:
    print("A")
elif obtainmarks>= 70:
    print("c")
else:
    print("you are fail and failer is the first step of success")

# Fifth  project:=
while True:
    num1 = int(input("Enter the first number:= "))
    num2 = int(input("Enter the second number:= "))
    print("1. Addition")
    print("2. Subtraction")
    print("3.Multiplication")
    print('4. division')
    chiose = int(input("Enter your chiose:= "))
    match chiose:
        case 1:
            print("Result:",num1 + num2)
        case 2:
            print("Result:",num1 - num2)
        case 3:
            print("Result:",num1 * num2)
        case 4:
            if num2 ==0:
                print("division cannot exist")
            else:
                print("okay")
            print("Result:",num1 / num2)
        case _:
            print("wrong chiose ")
# number six project:= 
def start_game():
    Gases_num = 27
    chance = 0

    while chance <5:
        chance = chance+1
        num = int(input("Enter gases number:="))
        if num<1 or num>50:
            print("Please enter a number between 1 and 50")
            continue
        elif num>Gases_num:
            print("you number is biggerthan gases number")
        elif num<Gases_num:
            print("Your number is lesserthan gases number")
        elif num ==Gases_num:
            print('You are winner! congralution')
            break
start_game()
# number seven project:=
def Check_password():
    secret_password = "python12345"
    chance = 0
    while chance<3:
        chance = chance+1
        Yourpassword = input("Enter your login password:= ")
        if Yourpassword == '':
            print("please enter your password empty is not Allowed")
            continue
        elif Yourpassword ==secret_password:
            print("you are successfully login ")
            break
        elif Yourpassword != secret_password:
            print("your password is wrong plese try again ")
Check_password()
# number eight project:=
def shopping_card():
    while True:
        Item_name = input("Enter shopping Item name:= ")
        if Item_name == 'end':
            print("Oky go for home its finish")
            break
        elif len(Item_name)< 3:
            print("This name is too short follow the game rules")
            continue
        elif len(Item_name)>=3:
            print("This is good you follow the game rule.")
shopping_card()
# project number nine:==
def word_counter():
    while True:
        a = input("Enter beautiful sentence:= ")
        if a == "exit":
            print("-:::::oky Good nigh swichup the light and sleep tight:::::-")
            break
        elif a == "":
            print("please input the sentence and follow the game rule")
            continue
        else:
            word_count = len(a.split())
        print("Total words in your sentence is:= ", word_count)
word_counter()
# project number ten:===
def virtual_bank_Account():
    currant_balance = 30000
    while True:
        print("1. For balancecheck")
        print("2.For Deposit")
        print("3.For Withdraw")
        print("4. For Exit")
        chiose = int(input("Enter your chiose:= "))
        match chiose:
            case 1:
                print("your currant balance in account is ",currant_balance)
            case 2:
                amount = int(input("Enter amount for deposit:= "))
                currant_balance += amount
                print("Successfully deposited! New balance is:=", currant_balance)
            case 3:

                Withdraw_balance = int(input("Enter amount to withdraw:= "))
                if currant_balance < Withdraw_balance:
                    print("Your balance is low")
                    continue
                else:
                    currant_balance -= Withdraw_balance
                    print("withdraw successfully! Remaining balance:", currant_balance)
                    

            case 4:
                    print("oky go to home your work done")
                    break
            case _:
                print("Inalid choice! Please try again.")
virtual_bank_Account()
# project number 11:-  
def show_menue():
    ''' this function to show menue'''
    while True:
        print("1. Biryani")
        print("2. Chicken Tikka ")
        print("3. Fried Rice")
        print("4. Burger ")
        print("5. pizza ")
        your_beautiful_oftion: int(input("Enter your prety dish"))
        match case :
            case 1:
                print("wow Biryani is Good option")
            case 2:
                print("wow Chicken Tikka is so Good option")
            case 3:
                print("Good Fried Rice is best for healt:::")
            case 4:
                print("you are burger boy ")
            case 5:
                Pizza_chiose =("1.large pizza or 2.small?  (option1 / option 2)")
                if Pizza_chiose == ' 1':
                    print("oky large pizza is best chiose")
                else:
                    print("oky small be is best chiose")
            case __:
                print("please select best option")
        name = input("Enter your name:= ")  
        age = input("Enter your age:= ")
        print(f"YOur name is{name}and your age is{age}")
        my_num = []
        for i in range(3):
            user_num = int(input(f"Enter number{i+1}:=="))
            if user_num < 0:
                print("only select positive number ")
                continue
            my_num.append(user_num)
        print("your beautiful list is:",my_num)
        break

show_menue()
# project number 12:- 
def Age_checker_program():
    while True:
        user_name = input("Enter your name please:-  ")
        user_age = int(input("Enter your age please:-  "))
        match user_age :
            case user_age if user_age <= 0:
                print("Invalid age only proceed for ages greater than 0.")
            case user_age if user_age >0 and user_age<=12:
                print(f'your name is {user_name} and your are chile your age is {user_age}')
            case user_age if user_age >12 and user_age<=17:
                print(f'your name is {user_name} and your are Teenager your age is {user_age}')
            case user_age if user_age >17 and user_age<=59:
                print(f'your name is {user_name} and your are Adult your age is {user_age} ')
            case user_age if user_age >= 60:
                print(f'your name is {user_name} and your are senior your age is {user_age} ')
            case(__):
                print("==:your are not put valid num:== ")
Age_checker_program()

        
            
        
            



        
    



        


                    



                

        


























           
    
    



  



