class Employee:
    min_experience=5
    def __init__(self,name,experience,department):
        self.name=name
        self.experience=experience
        self.department=department
    def eligible_for_promotion(self):
        if self.experience >= Employee.min_experience:
            return "Eligible For Promotion"
        else:
            return "Not Eligible For Promotion"
    @classmethod
    def update_promotion_criteria(cls,years):
        cls.min_experience=years
    @staticmethod
    def is_valid_department(department):
        valid_departments=["HR","TECH","ADMIN","MANAGER"]
        return department in valid_departments
    def display(self):
        print("NAME:",self.name)
        print("EXPERIENCE:",self.experience,"YEARS")
        print("DEPARTMENT:",self.department)
        print("PROMOTION STATUS:",self.eligible_for_promotion())
        print("DEPARTMENT VALID:",Employee.is_valid_department(self.department))
        print()
s1=Employee("GANESH",6,"HR")
s2=Employee("KUMAR",8,"MANAGER")
s3=Employee("TARUN",9,"CUSTOMER SUPPORT")
departments=[s1,s2,s3]
print("BEFORE UPDATING PROMOTION CRITERIA:")
for department in departments:
    department.display()
Employee.update_promotion_criteria(8)
print("AFTER UPDATING PROMOTION CRITERIA TO 8 YEARS:")
for department in departments:
    department.display()


