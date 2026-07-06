class Employee:
    company_name="Techcorp"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
Employee1=Employee("Kumar")
Employee2=Employee("Sankar")
print("Before Update Class:")
print(Employee1.name,"-",Employee1.company_name)
print(Employee2.name,"-",Employee2.company_name)
Employee.change_company("Cvcorp")
print("After Update Class:")
print(Employee1.name,"-",Employee1.company_name)
print(Employee2.name,"-",Employee2.company_name)
