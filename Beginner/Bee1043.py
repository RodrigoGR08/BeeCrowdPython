#Read three point floating values (A, B and C) and verify if is possible to make a triangle with them. If it is possible, calculate the perimeter of the triangle and print the message:

#Perimetro = XX.X

#If it is not possible, calculate the area of the trapezium which basis A and B and C as height, and print the message:

#Area = XX.X
A,B,C = map(float,input().split())
if A+B>C and A+C>B and B+C>A:
    print(f'Perimetro = {A+B+C:.1f}')
else:
    print(f'Area = {((A+B)*C)/2:.1f}')
