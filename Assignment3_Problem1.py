class Employee:
    # Class variable to count the number of Employees
    employee_count = 0
    
    def __init__(self, name, family, salary, department):
        # Instance variables
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        # Increment the employee count
        Employee.employee_count += 1
    
    def average_salary(self, *salaries):
        total_salary = sum(salaries) + self.salary
        average_salary = total_salary / (len(salaries) + 1)
        return average_salary

class FullTimeEmployee(Employee):
    # Additional property specific to FullTimeEmployee
    def __init__(self, name, family, salary, department, hours_per_week):
        # Call the constructor of the parent class
        super().__init__(name, family, salary, department)
        # Instance variable specific to FullTimeEmployee
        self.hours_per_week = hours_per_week

# Creating instances of Employee and FullTimeEmployee classes
employee1 = Employee("Sai Kumar", "Family1", 50000, "HR")
employee2 = FullTimeEmployee("Jishitha", "Family2", 60000, "IT", 40)

# Calling member functions
average_salary_result = employee1.average_salary(55000, 60000)
print(f"Average Salary for {employee1.name}: ${average_salary_result}")

print(f"Total Number of Employees: {Employee.employee_count}")

print(f"Full-Time Employee Name: {employee2.name}, Hours per Week: {employee2.hours_per_week}")
