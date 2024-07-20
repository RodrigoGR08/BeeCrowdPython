#Make a program that reads three floating point values: A, B and C. Then, calculate and show:
#a) the area of the rectangled triangle that has base A and height C.
#b) the area of the radius's circle C. (pi = 3.14159)
#c) the area of the trapezium which has A and B by base, and C by height.
#d) the area of ​​the square that has side B.
#e) the area of the rectangle that has sides A and B.
pi = 3.14159
values = input()
values = values.split()
a = float(values[0])
b = float(values[1])
c = float(values[2])
areaOfTriangle = (a*c)/2
areaOfCircle = pi*(c**2)
areaOfTrapezium = ((a+b)/2)*c
areaOfSquare = b**2
areaOfRectangle = a*b
print(f"""TRIANGULO: {areaOfTriangle:.3f}
CIRCULO: {areaOfCircle:.3f}
TRAPEZIO: {areaOfTrapezium:.3f}
QUADRADO: {areaOfSquare:.3f}
RETANGULO: {areaOfRectangle:.3f}""")
