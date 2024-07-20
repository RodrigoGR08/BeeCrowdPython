#Read the four values corresponding to the x and y axes of two points in the plane, p1 (x1, y1) and p2 (x2, y2) and calculate the distance between them, showing four decimal places, according to the formula:
#Distance = ((x2-x1)**2) + ((y2-y1)**2))**0.5

firstValues = input()
firstValues = firstValues.split()
x1 = float(firstValues[0])
y1= float(firstValues[1])
secondValues = input()
secondValues = secondValues.split()
x2 = float(secondValues[0])
y2= float(secondValues[1])
xDifference = (x2-x1)**2
yDifference = (y2-y1)**2
distance = ((xDifference)+(yDifference))**0.5
print(f'{distance:.4f}')