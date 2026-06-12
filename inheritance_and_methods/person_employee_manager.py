"""
## 5. Person -> Employee -> Manager (Multi-Level Inheritance)  *(Hard)*

=================================================
PERSON -> EMPLOYEE -> MANAGER
(MULTI-LEVEL INHERITANCE + METHOD TYPES)
=================================================

Problem Statement:
Build a THREE-LEVEL inheritance chain:

   Person          (level 1 — base)
   └── Employee    (level 2 — inherits Person)
       └── Manager (level 3 — inherits Employee)

Each level ADDS its own NEW methods and
attributes. NO method on the parent should be
OVERRIDDEN — every child must extend its
parent ONLY by introducing new behaviour, and
must call super().__init__() to reuse the
parent's constructor.

This problem teaches:
   - multi-level inheritance
   - super().__init__() in every level
   - instance / class / static method types
   - one class can use methods INHERITED from
     ALL its ancestors (without overriding)

-------------------------------------------------
Instructions:

Person (level 1)
   class attribute is:
       species = "Homo sapiens"

   __init__(self, name, age):
       self.name = name
       self.age  = age

   greet(self) -> str:
       return f"Hi, I'm {self.name}, age {self.age}"

   @staticmethod
   def is_adult(age) -> bool:
       return age >= 18

Employee (level 2, inherits Person)
   class attribute is:
       company   = "Acme Corp"
       bonus_pct = 5

   __init__(self, name, age, emp_id, salary):
       - call super().__init__(name, age)
       - store emp_id and salary

   work_intro(self) -> str:
       return (f"I work at {Employee.company} "
               f"as id {self.emp_id}")

   apply_bonus(self):
       self.salary += self.salary * Employee.bonus_pct / 100

   @classmethod
   def set_bonus(cls, new_pct):
       cls.bonus_pct = new_pct

Manager (level 3, inherits Employee)
   __init__(self, name, age, emp_id, salary, team):
       - call super().__init__(name, age, emp_id, salary)
       - store team (a LIST of Employee objects)

   add_member(self, employee):
       - append to self.team

   team_intro(self) -> str:
       return f"I lead a team of {len(self.team)} people."

   team_total_salary(self) -> float:
       - return self's salary PLUS the sum of
         every team member's salary
       (use a for loop to walk self.team)

In the driver code:
   - create one Person and call greet()
   - create two Employee objects, and on each
     call greet() (inherited from Person) AND
     work_intro() (defined in Employee)
   - create one Manager, add the two Employee
     objects to her team, and call
     greet()      (inherited from Person)
     work_intro() (inherited from Employee)
     team_intro() (defined in Manager)
   - call apply_bonus() on every employee
     INCLUDING the manager
     (Manager inherits apply_bonus from
      Employee unchanged)
   - call Employee.set_bonus(10) to change
     the class-wide bonus percentage, then
     call apply_bonus() again to confirm BOTH
     subclasses see the new value
   - call Person.is_adult(age) with several
     ages, including ones from the objects
   - call m.team_total_salary() and print it

Do NOT use:
   - any external library
   - global keyword
   - method overriding (each child must only
     ADD new methods, not redefine any of the
     parent's methods)
   - manually rewriting parent __init__ logic
     in the child (must use super())

-------------------------------------------------
Input Example:
p = Person("Sam", 17)

e1 = Employee("Alice", 25, "E001", 100000)
e2 = Employee("Bob",   30, "E002", 80000)

m  = Manager("Carol", 40, "M001", 150000, [])
m.add_member(e1)
m.add_member(e2)

e1.apply_bonus()
e2.apply_bonus()
m.apply_bonus()                      # inherited from Employee
Employee.set_bonus(10)
m.apply_bonus()                      # inherited, now at 10%

Output Example (representative):
Hi, I'm Sam, age 17

Hi, I'm Alice, age 25
I work at Acme Corp as id E001

Hi, I'm Bob, age 30
I work at Acme Corp as id E002

Hi, I'm Carol, age 40
I work at Acme Corp as id M001
I lead a team of 2 people.

Alice salary -> 105000.0
Bob   salary -> 84000.0
Carol salary -> 157500.0   # one 5% bonus
Carol salary -> 173250.0   # one 10% bonus on top

is_adult(17) -> False
is_adult(25) -> True

Team total salary -> 173250.0 + 105000.0 + 84000.0

=================================================

"""
class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age  = int(age)

    def greet(self):
        return f"Hi, I'm {self.name}, age {self.age}"

    @staticmethod
    def is_adult(age):
        return int(age) >= 18

class Employee(Person):
    company   = "Acme Corp"
    bonus_pct = 5

    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = float(salary)

    def work_intro(self):
        return (f"I work at {Employee.company} "
                f"as id {self.emp_id}")

    def apply_bonus(self):
        self.salary += self.salary * Employee.bonus_pct / 100

    @classmethod
    def set_bonus(cls, new_pct):
        cls.bonus_pct = new_pct

class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, team=None):
        super().__init__(name, age, emp_id, salary)
        self.team = team if team is not None else []

    def add_member(self, employee):
        self.team.append(employee)

    def team_intro(self):
        return f"I lead a team of {len(self.team)} people."

    def team_total_salary(self):
        total_salary = self.salary
        for member in self.team:
            total_salary += member.salary
        return total_salary

person_name = input("Enter Person's name: ")
person_age = input("Enter Person's age: ")
p = Person(person_name, person_age)
print(p.greet())

emp1_name = input("Enter first Employee's name: ")
emp1_age = input("Enter first Employee's age: ")
emp1_id = input("Enter first Employee's ID: ")
emp1_salary = input("Enter first Employee's salary: ")
e1 = Employee(emp1_name, emp1_age, emp1_id, emp1_salary)

emp2_name = input("Enter second Employee's name: ")
emp2_age = input("Enter second Employee's age: ")
emp2_id = input("Enter second Employee's ID: ")
emp2_salary = input("Enter second Employee's salary: ")
e2 = Employee(emp2_name, emp2_age, emp2_id, emp2_salary)

print(e1.greet())
print(e1.work_intro())
print(e2.greet())
print(e2.work_intro())

manager_name = input("Enter Manager's name: ")
manager_age = input("Enter Manager's age: ")
manager_id = input("Enter Manager's ID: ")
manager_salary = input("Enter Manager's salary: ")
m = Manager(manager_name, manager_age, manager_id, manager_salary)
m.add_member(e1)
m.add_member(e2)

print(m.greet())
print(m.work_intro())
print(m.team_intro())

print(f"{e1.name} salary before bonus: {e1.salary}")
print(f"{e2.name} salary before bonus: {e2.salary}")
print(f"{m.name} salary before bonus: {m.salary}")

e1.apply_bonus()
e2.apply_bonus()
m.apply_bonus()

print(f"{e1.name} salary after first bonus (5%): {e1.salary}")
print(f"{e2.name} salary after first bonus (5%): {e2.salary}")
print(f"{m.name} salary after first bonus (5%): {m.salary}")

new_bonus_pct = input("Enter new bonus percentage: ")
Employee.set_bonus(int(new_bonus_pct))

e1.apply_bonus()
e2.apply_bonus()
m.apply_bonus()

print(f"{e1.name} salary after second bonus ({new_bonus_pct}%): {e1.salary}")
print(f"{e2.name} salary after second bonus ({new_bonus_pct}%): {e2.salary}")
print(f"{m.name} salary after second bonus ({new_bonus_pct}%): {m.salary}")

age_test1 = input("Enter an age to test for adulthood: ")
print(f"is_adult({age_test1}) -> {Person.is_adult(age_test1)}")
age_test2 = input("Enter another age to test for adulthood: ")
print(f"is_adult({age_test2}) -> {Person.is_adult(age_test2)}")

print(f"Team total salary -> {m.team_total_salary()}")