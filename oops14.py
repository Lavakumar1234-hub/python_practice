class Loan:
    interest_rate=10
    def __init__(self,borrower_name,principal):
        self.borrower_name=borrower_name
        self.principal=principal
    def total_payable_amount(self):
        return self.principal+(self.principal*Loan.interest_rate/100)
    @classmethod
    def update_interest_rate(cls,new_interest):
        cls.interest_rate=new_interest
    @staticmethod
    def check_loan_eligibility(salary):
        return salary>25000
    def display(self):
        print("BORROWER NAME:",self.borrower_name)
        print("PRINCIPAL:",self.principal)
        print("TOTAL PAYABLE:",self.total_payable_amount())
        print()
s1=Loan("KRISHNA",50000)
s2=Loan("GANESH",30000)
s3=Loan("KUMAR",25000)
loans=[s1,s2,s3]
print("BEFORE UPDATING INTEREST RATE:")
for loan in loans:
    loan.display()
print("LOAN ELIGIBILITY:")
print(f"{s1.borrower_name}(SALARY - {s1.principal}):",Loan.check_loan_eligibility(s1.principal))
print(f"{s2.borrower_name}(SALARY - {s2.principal}:",Loan.check_loan_eligibility(s2.principal))
print(f"{s3.borrower_name}(SALARY - {s3.principal}:",Loan.check_loan_eligibility(s3.principal))
print()
Loan.update_interest_rate(18)
print("AFTER UPDATING INTEREST RATE TO 18%:")
for loan in loans:
    loan.display()