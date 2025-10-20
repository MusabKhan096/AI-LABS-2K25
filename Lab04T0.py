class Person:
    name = "Musa'b Khan"
    age = 20
class Job:
    designation = "Cyber Analyst"
    salary = 70000
class Employee(Person, Job):
    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Designation:", self.designation)
        print("Salary:", self.salary)
emp = Employee()
print("==========================")
emp.name = "Musa'b Khan"
emp.age = 20
emp.designation = "Cyber Analyst"
emp.salary = 70000
emp.show()
print("==========================")