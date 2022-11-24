from datetime import datetime   # to work with date you must import datetime module 
import random # The import random loads the random module
#  a module is a file consisting of Python code. It can define functions, classes, and variables

data = {'3665935030': {'name': 'Desmond', 'dob': '31/21/21', 'bvn': '23456789', 'pin': '1234', 'bal': 185000}} # data is  
#(line 5)   a variable assigned to a value, and this above is a nested dictionary

trans_data = {'3665935030': 
    [{'amount': 200000, 'type': 'credit', 'action': 'deposit', 'date': datetime.strptime('13-02-2022', ).date()}, 
     {'amount': 12000, 'type': 'debit', 'action': 'withdrawal', 'date': datetime.strptime('14-02-2022',"%d-%m-%Y").date()},
     {'amount': 3000, 'type': 'debit', 'action': 'withdrawal', 'date': datetime.strptime('19-02-2022',"%d-%m-%Y").date()}]}

def get_stats(start_date:datetime, end_date:datetime, transactions:list): # def means defining a funtiong which means get_stats is a function
    """_summary_
(this comment is  a docstring) 
    Args: (argument)
        start_date (datetime): _description_
        end_date (datetime): _description_
        transactions (list): _description_
    """
    lower_limit = filter(lambda x:x['date']>=start_date, transactions) #lambda function can take any number of arguments, but can only have one expression.
    
    main_data = list(filter(lambda x:x['date']<=end_date, lower_limit)) #filter is a class or a function
    
    print(f"\nYour statement of account from {datetime.strftime(start_date, '%d-%b-%Y')} to {datetime.strftime(end_date, '%d-%b-%Y')} is given below:") #d,b,y stands for short version of date,month,year
    for data in main_data:# in is to check if an item is presents in an iterable while for is a loop
        print(f"\nDate: {datetime.strftime(data['date'], '%d-%b-%Y')}")
        print(f"Amount: ${data['amount']}")
        print(f"Transaction Type: {data['type'].title()}")
        print(f"Action: {data['action'].title()}")
        
    #getting the average credits and debits
    credit = [data['amount'] for data in main_data if data['type']=='credit']
    debit = [data['amount'] for data in main_data if data['type']=='debit']
    
    try: # The try block lets you test a block of code for errors
        average_credit = round(sum(credit)/len(credit), 3)
        print(f"The average credit during this period was ${average_credit}")
    except ZeroDivisionError: #t defines a block of code to run if the try block raises an error.
        print("The average credit during this period was $0.00")
        
    try:
        average_debit = round(sum(debit)/len(debit),3)
        print(f"The average debit during this period was ${average_debit}")
    except ZeroDivisionError:
        print("The average debit during this period was $0.00")
    
    return # return keyword is to exit a function and return a value.


print("Welcome to the AstroBank App")
while True: #To create a while loop, 	Boolean value, result of comparison operations
    print("Enter s to signup or l to login:")
    print("Enter any other key to close")
    choice = input(">").lower()

    if choice == 'l':
        acc_num = input("Enter your account num:\n>") # input function very common an will always change any item in it to a string
        pin = input("Enter your pin:\n>")
        
        user = data.get(acc_num) # get() method returns the value of the item with the specified key in a dictionary
        
        if user and user['pin'] == pin: #  if  is To make a conditional statement, and is A logical operator
            print(f"Welcome {user['name']}.\nYour account balance is ${user['bal']}")
            
            while True:
                print("""\nWhat would you like to do?
                    Press 1 to withdraw
                    Press 2 to deposit
                    Press 3 to transfer
                    Press any other key to quit.""")
                
                user_input = input(">")
                
                if user_input == '1':
                    amount = int(input("How much?\n>"))
                    if amount >= user['bal']:
                        print("Insufficient Funds")
                    else: #else	Used in conditional statements
                        user['bal']-=amount
                        
                        #log transaction data
                        detail = {
                            "amount":amount,
                            "type": "debit",
                            "action" : "withdrawal",
                            "date" : datetime.now().date()
                            
                        }
                        
                        trans_data[acc_num].append(detail) #append is used to add an item to a list
                        
                        
                        print("Please take your cash")
                        print(f"Balance is {user['bal']}")
                        
                elif user_input == '2': #elif	Used in conditional statements, same as else if
                    amount = int(input("How much?\n>")) #int is a short version of integer
                    
                    user['bal']+=amount
                    
                    #log transaction data
                    detail = {
                        "amount":amount,
                        "type": "credit",
                        "action" : "deposit",
                        "date" : datetime.now().date()
                    }
                    
                    trans_data[acc_num].append(detail)
                        
                    print("Successful")
                    print(f"Balance is {user['bal']}")
                elif user_input == '3':
                    recepient_ = input("Enter recepient account\n>")
                    amount = int(input("How much?\n>"))
                    
                    if user['bal'] < amount:
                        print("Insufficient Funds")
                    
                    recepient = data.get(recepient_)
                    if recepient:
                        recepient['bal'] += amount
                        user['bal'] -=amount
                        
                        #log transaction data
                        detail = {
                            "amount":amount,
                            "type": "debit",
                            "action" : "transfer",
                            "date" : datetime.now().date()
                        }
                        
                        trans_data[acc_num].append(detail)
                        
                        detail_recepient = {
                            "amount":amount,
                            "type": "credit",
                            "action" : "transfer",
                            "date" : datetime.now().date()
                        }
                        
                        trans_data[recepient_].append(detail_recepient)
                        
                        print("Successful")
                        print(f"Balance is {user['bal']}")
                    else:
                        print(f"Unable to fetch customer with account {recepient_}")
                elif user_input == '4':
                    
                    #get the start and end date. Using strptime method, convert the inputed string into datetime object.
                    start_date = datetime.strptime(input("Enter start date(dd-mm-yyyy)\n>"), "%d-%m-%Y").date()
                    end_date = datetime.strptime(input("Enter end date(dd-mm-yyyy)\n>"), "%d-%m-%Y").date()
                    #get the transaction from the trans_data dictionary
                    trans = trans_data[acc_num]
                    
                    # print(start_date)
                    # print(end_date)
                    # print(trans)
                    
                    get_stats(start_date, end_date, trans)
                          
                else:
                    print("Good bye")
                    break # break	To break out of a loop      
        else:
            print("Invalid Login")
            
    elif choice == 's':
        name = input("Enter your name:\n>")
        dob= input("Enter your date of birth:\n>")
        bvn= input("Enter your BVN:\n>")
        pin = input("Enter your PIN:\n>")
        details = [('name', name), 
                ('dob', dob), 
                ('bvn', bvn), 
                ('pin', pin), 
                ('bal',0) 
                ]
    
        #generate account number
        num = [1,2,3,4,5,6,7,8,9,0]
        acc_num_list = ["3"]
        acc_num_list.extend([str(random.choice(num)) for _ in range(9)])
        
        
        acc_num = "".join(acc_num_list)
        
        data[acc_num] = dict(details)
        trans_data[acc_num] = []
        
        print(f"\nYour account has been created. You account number is {acc_num}\n")

    else:
        break



# print(data)
# print(trans_data)