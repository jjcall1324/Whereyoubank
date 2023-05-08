import mysql.connector
cnx = mysql.connector.connect(user = 'root', password = 'jjcall13', host = '127.0.0.1', database = 'Bank', )

def create_account(cnx):
    username = input("Enter username: ")
    password = input("Enter password: ")
    initial_balance = float(input("Enter initial balance: "))
    cursor = cnx.cursor()
    add_account = ("INSERT INTO Account "
                   "(username, password, balance) "
                   "VALUES (%s, %s, %s)")
    data_account = (username, password, initial_balance)
    cursor.execute(add_account, data_account)
    account_id = cursor.lastrowid

   
    add_balance = ("INSERT INTO AccountBalance "
                   "(accountID, balance) "
                   "VALUES (%s, %s)")
    data_balance = (account_id, initial_balance)
    cursor.execute(add_balance, data_balance)

    cnx.commit()
    cursor.close()

    print(f"Account {username} created successfully with initial balance of {initial_balance}. Id {account_id}")
    
def deposit_money(cnx):
    # Get user input for deposit information
    username = input("Enter account username: ")
    password = input("Enter account password: ")
    deposit_amount = float(input("Enter deposit amount: "))

    # Verify account using username and password
    cursor = cnx.cursor()
    query = ("SELECT * FROM Account WHERE username = %s AND password = %s")
    data = (username, password)
    cursor.execute(query, data)
    account = cursor.fetchone()

    if account is None:
        print("Invalid username or password.")
        return

    # Update balance in "AccountBalance" table
    account_id = account[0]
    query = ("UPDATE AccountBalance SET balance = balance + %s WHERE accountID = %s")
    data = (deposit_amount, account_id)
    cursor.execute(query, data)

    # Insert deposit record into "Deposit" table
    query = ("INSERT INTO Deposit (accountID, amount) VALUES (%s, %s)")
    data = (account_id, deposit_amount)
    cursor.execute(query, data)

    # Commit changes to database and close cursor
    cnx.commit()
    cursor.close()

    print(f"Deposit of {deposit_amount} successfully made to account {account_id}.")
    
def withdraw_money(cnx):
    # Get user input for withdrawal information
    username = input("Enter account username: ")
    password = input("Enter account password: ")
    withdrawal_amount = float(input("Enter withdrawal amount: "))

    # Verify account using username and password
    cursor = cnx.cursor()
    query = ("SELECT * FROM Account WHERE username = %s AND password = %s")
    data = (username, password)
    cursor.execute(query, data)
    account = cursor.fetchone()

    if account is None:
        print("Invalid username or password.")
        return

    # Check if there is enough money in the account to make the withdrawal
    account_id = account[0]
    query = ("SELECT balance FROM AccountBalance WHERE accountID = %s")
    data = (account_id,)
    cursor.execute(query, data)
    balance = cursor.fetchone()[0]

    if balance < withdrawal_amount:
        print("Insufficient funds.")
        return

    # Update balance in "AccountBalance" table
    query = ("UPDATE AccountBalance SET balance = balance - %s WHERE accountID = %s")
    data = (withdrawal_amount, account_id)
    cursor.execute(query, data)

    # Insert withdrawal record into "Withdrawal" table
    query = ("INSERT INTO Withdrawal (accountID, amount) VALUES (%s, %s)")
    data = (account_id, withdrawal_amount)
    cursor.execute(query, data)

    # Commit changes to database and close cursor
    cnx.commit()
    cursor.close()

    print(f"Withdrawal of {withdrawal_amount} successfully made from account {account_id}.")
def check_balance(cnx):
    # Get user input for account information
    username = input("Enter account username: ")
    password = input("Enter account password: ")

    # Verify account using username and password
    cursor = cnx.cursor()
    query = ("SELECT * FROM Account WHERE username = %s AND password = %s")
    data = (username, password)
    cursor.execute(query, data)
    account = cursor.fetchone()

    if account is None:
        print("Invalid username or password.")
        return

    # Get account balance from "AccountBalance" table
    account_id = account[0]
    query = ("SELECT balance FROM AccountBalance WHERE accountID = %s")
    data = (account_id,)
    cursor.execute(query, data)
    balance = cursor.fetchone()[0]

    # Close cursor
    cursor.close()

    print(f"Account {account_id} has a balance of {balance}.")
def login(cnx):
    # Get user input for login information
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Verify login information
    cursor = cnx.cursor()
    query = ("SELECT * FROM Account WHERE username = %s AND password = %s")
    data = (username, password)
    cursor.execute(query, data)
    account = cursor.fetchone()

    if account is None:
        print("Invalid username or password.")
        return

    # Close cursor
    cursor.close()

    print(f"Welcome, {account[1]}!")
    
def menu():
    print("[1] Create an account: ")
    print("[2] Deposit: ")
    print("[3] Withdraw ")
    print("[4] Check Balance")
    print("[5] Login in ")
    print("[6] Exit Program")

menu()
option = int(input("enter your option: "))

while option != 6: 
    if option == 1:
        create_account(cnx)
    elif option == 2:
        deposit_money(cnx)
    elif option == 3:
        withdraw_money(cnx)
    elif option == 4:
        check_balance(cnx)
    elif option == 5:
        login(cnx)
    else:
        print("invalied option. ")

    print()    
    menu()
    option = int(input("enter your option: "))

print("Thank for using this program goodbye")