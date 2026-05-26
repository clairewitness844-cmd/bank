import random as rnd
import datetime as dt

class Bank_account():
    def __init__(self, account_fname,account_lname,ID_no,balance=0,account_type="Savings"):
        self.account_fname=account_fname
        self.account_lname=account_lname
        self.ID_no=ID_no
        self.balance=balance
        self.account_type = account_type
        self.account_no = self.create_account_no()
        self.transactions = []
        self._add_transaction("account created", balance)

    def create_account_no(self):
        return f"{rnd.randint(100001,999999)}-{self.ID_no}"
        
    def check_balance(self):
        return self.balance
    
    def withdraw(self,withdraw_amount):
        
        try:
            withdraw_amount=int(withdraw_amount)
        except:
            return "enter an integer value"
        
        if withdraw_amount<=0:
            return "amount needs to be a positive value"
        if withdraw_amount>self.balance:
            return "insufficient funds"
        
        self.balance-=withdraw_amount
        self._add_transaction("Withdrawal", withdraw_amount)

        return self.balance
    
    def deposit(self,deposit_amount):
        
        try:
            deposit_amount=int(deposit_amount)
        except:
            return "amount must be an integer"
        
        if deposit_amount<0:
            self.withdraw()
            return f"transaction of {deposit_amount} has switched to withdrawal"
        
        self.balance+=deposit_amount
        self._add_transaction("deposit", deposit_amount)
        return self.balance
    
    def _add_transaction(self, action, amount):
        timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append({
            "time": timestamp,
            "action": action,
            "amount": amount,
            "balance_after": self.balance
        })
        return self.transactions
    
    def get_account_type(self):
        return self.account_type
    def choose_account(self):
        print(""" choose:
              1. Chequeing account 
              2. savings account 
              3. investement account 
    """)
        user_selection=int(input("choose account type"))
        if user_selection==1:
            self.account_type="Chequeing"
        elif user_selection==2:
            self.account_type="Savings"
        elif user_selection==3:
            self.account_type="Investment"
        else: 
            print("invalid choice, defaulting to savings")
            self.account_type="Savings"
        
    def get_transaction_history(self):
        return self.transactions

    def get_account_number(self):
        return self.account_no

    def get_holder_name(self):
        return f"{self.account_fname} {self.account_lname}"

def main():
     fname=input("Enter your first name:\t").title()
     lname=input("Enter you last name:\t").capitalize()
     ID=input("enter your ID number")
     
     account = Bank_account(fname, lname, ID)
     account_type=account.choose_account()
     print("\nAccount created successfully!")
     print(f"""*******holder namer:\t {account.get_holder_name()}******
                                    Account number:\t {account.get_account_number()}
                                    Account type:\t {account.get_account_type()}""")
     while True:
         print("""pick 
    1 Deposit
    2 Withdraw
    3 Balance chec
    4 Transaction history
    5. Exit
    """)
         current_transaction=int(input("enter your choice: \t"))
                                   
         if current_transaction==1:
            amt=input("amount to deposit:\t ")
            print ("new balance:\t", account.deposit(amt))
         elif current_transaction==2:
            amt=input("amount to withdraw")
            print ("new balance:\t", account.withdraw(amt))
         elif current_transaction==3:
            print("your account balance is:\t ", account.check_balance())
         elif current_transaction==4:
            for t in account.get_transaction_history():
                print(t)
         elif current_transaction==5:
            print("exiting.......")
            break
         else:
            print("invalid choice")
main()