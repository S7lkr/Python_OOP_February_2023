class Employee:
    _MONTHS = 12

    def __init__(self, name_id: int, first_name: str, last_name: str, salary: int):
        self.id = name_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self) -> int:
        return Employee._MONTHS * self.salary

    def raise_salary(self, amount) -> int:
        self.salary += amount
        return self.salary


employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())