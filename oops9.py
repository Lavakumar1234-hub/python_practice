class BankAccount:
    bank_name="ABC Bank"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
        print(f"New Name of The Bank:{cls.bank_name}")
    @staticmethod
    def validate_amount(amount):
        return amount>0
    def deposit(self,amount):
        if BankAccount.validate_amount(amount):
            self.balance+=amount
            print(f"{amount} deposit Successfully.")
            print(f"New Balance of {self.holder}: {self.balance}")
        else:
            print("Invalid deposit Amount!")
bankaccount1=BankAccount("kumar",5000)
bankaccount2=BankAccount("murali",7000)
bankaccount3=BankAccount("kiran",8000)
print(f"Initial Bank name:{BankAccount.bank_name}")
bankaccount1.deposit(1000)
bankaccount2.deposit(1500)
bankaccount3.deposit(-500)
BankAccount.change_bank_name("State Bank of India")
print("After Changing Bank Name:")
print(f"{bankaccount1.holder}'s Bank:{bankaccount1.bank_name}")
print(f"{bankaccount2.holder}'s Bank:{bankaccount1.bank_name}")
print(f"{bankaccount3.holder}'s Bank:{bankaccount3.bank_name}")

