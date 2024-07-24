# In an imaginary country called Lisarb, all the people are very happy to pay their taxes because they know that doesn’t exist corrupt politicians and the taxes are used to benefit the population, without any misappropriation. The currency of this country is Rombus, whose symbol is R$.

# Read a value with 2 digits after the decimal point, equivalent to the salary of a Lisarb inhabitant. Then print the due value that this person must pay of taxes, according to the table below.


salary = float(input(""))
if salary <= 2000.00:
    print("Isento")
elif salary > 2000.00 and salary <= 3000.00:
    rest = salary - 2000
    tax = rest * 0.08
    print(f'R$ {tax:.2f}')
elif salary > 3000.00 and salary <= 4500.00:
    rest = salary - 3000
    tax = (rest*0.18)+(1000*0.08)
    print(f'R$ {tax:.2f}')
elif salary >4500.00:
    rest = salary - 4500
    tax = (rest*0.28)+(1500*0.18)+(1000*0.08)
    print(f'R$ {tax:.2f}')
