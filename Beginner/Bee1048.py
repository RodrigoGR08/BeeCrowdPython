# The company ABC decided to give a salary increase to its employees, according to the following table:


# Salary	Readjustment Rate
# 0 - 400.00
# 400.01 - 800.00
# 800.01 - 1200.00
# 1200.01 - 2000.00
# Above 2000.00

# 15%
# 12%
# 10%
# 7%
# 4%


# Read the employee's salary, calculate and print the new employee's salary, as well the money earned and the increase percentual obtained by the employee, with corresponding messages in Portuguese, as the below example.

salary = float(input())

if salary > 0 and salary <= 400.00:
    newPercentage = 15
    newSalary = salary + ((salary*newPercentage)/100)
elif salary > 400.00 and salary <= 800.00:
    newPercentage = 12
    newSalary = salary + ((salary*newPercentage)/100)
elif salary >800.00 and salary <=1200.00:
    newPercentage = 10
    newSalary = salary + ((salary*newPercentage)/100)
elif salary >1200.00 and salary <=2000.00:
    newPercentage = 7
    newSalary = salary + ((salary*newPercentage)/100)
else:
    newPercentage = 4
    newSalary = salary + ((salary*newPercentage)/100)

print(f'Novo salario: {newSalary:.2f}\nReajuste ganho: {((salary*newPercentage)/100):.2f}\nEm percentual: {newPercentage} %')