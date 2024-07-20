#Read 3 floating-point numbers. 
# After, print the roots of bhaskara’s formula. 
# If it's impossible to calculate the roots because a division by zero or a square root of a negative number, presents the message “Impossivel calcular”.

import math
values = input()
values = values.split()
A = float(values[0])
B = float(values[1])
C = float(values[2])
delta = (B**2)-(4*A*C)
division = 2*A
if division <= 0 or delta<0:
    print("Impossivel calcular")
else:  
    finalRoot = math.sqrt(delta)
    R1 = (-B+finalRoot)/division
    R2 = (-B-finalRoot)/division
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')