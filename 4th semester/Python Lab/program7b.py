class employee:
    total = 0

    def __init__(self, name, id, dept, salary):
        self.name = name
        self.id = id
        self.dept = dept
        self.salary = salary
        self.total += 1

    def update_salary(self, percent):
        self.salary = self.salary + self.salary * percent / 100

    def display(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("Department:", self.dept)
        print("Salary:", self.salary)


emp = []
n = int(input("Enter no. of employees:"))
if n < 1:
    print("Invalid value")
    exit()
for x in range(n):
    name = input("Enter name %d:" % (x + 1))
    eid = input("Enter id %d:" % (x + 1))
    dept = input("Enter department %d:" % (x + 1))
    salary = int(input("Enter salary %d:" % (x + 1)))
    emp.append(employee(name, eid, dept, salary))
    print("\n")
dept = input("Enter department:")
hike = int(input("Hike percentage:"))
if hike > 100 or hike < 0:
    print("Invalid")
    exit()
for x in range(n):
    if dept == emp[x].dept:
        emp[x].update_salary(hike)
for x in range(n):
    emp[x].display()
    print("\n")
