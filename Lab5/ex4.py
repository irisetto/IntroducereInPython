
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def display_info(self, position):
        return f"{position}: {self.name} -> {self.salary} lei"

    def get_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_department(self):
        return self.department

class Engineer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def get_language(self):
        return self.language

class Salesperson(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def make_sale(self):
        return f"{self.name} made a sale."

def main():
    manager = Manager(name="Alice", salary=50000, department="Sales")
    print(manager.display_info(manager.__class__.__name__))
    print("Departament: ",manager.get_department())

    engineer = Engineer(name="Bob", salary=60000, language="Python")
    print(engineer.display_info(engineer.__class__.__name__))
    print("Preferred programming language: " , engineer.get_language())

    salesperson = Salesperson(name="Charlie", salary=40000)
    print(salesperson.display_info(salesperson.__class__.__name__))
    print(salesperson.make_sale())

if __name__ == "__main__":
    main()