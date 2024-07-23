#Read 3 double numbers (A, B and C) representing the sides of a triangle and arrange them in decreasing order, so that the side A is the biggest of the three sides. Next, determine the type of triangle that they can make, based on the following cases always writing an appropriate message:

#if A ≥ B + C, write the message: NAO FORMA TRIANGULO
#if A2 = B2 + C2, write the message: TRIANGULO RETANGULO
# if A2 > B2 + C2, write the message: TRIANGULO OBTUSANGULO
# if A2 < B2 + C2, write the message: TRIANGULO ACUTANGULO
# if the three sides are the same size, write the message: TRIANGULO EQUILATERO
# if only two sides are the same and the third one is different, write the message: TRIANGULO ISOSCELES

A, B, C = map(float, input().split())
values = [A, B, C]
decreasingValues = values[:]

for i in range(0, len(decreasingValues)):
    for j in range(i+1, len(decreasingValues)):
        if decreasingValues[i] < decreasingValues[j]:
            decreasingValues[i], decreasingValues[j] = decreasingValues[j], decreasingValues[i]

if decreasingValues[0] >= decreasingValues[1]+decreasingValues[2]:
    print("NAO FORMA TRIANGULO")
elif (decreasingValues[0])**2 == ((decreasingValues[1])**2) + ((decreasingValues[2])**2):
    print("TRIANGULO RETANGULO")
elif (decreasingValues[0])**2 > ((decreasingValues[1])**2) + ((decreasingValues[2])**2):
    print("TRIANGULO OBTUSANGULO")
elif (decreasingValues[0])**2 < ((decreasingValues[1])**2) + ((decreasingValues[2])**2):
    print("TRIANGULO ACUTANGULO")

if decreasingValues[0] == decreasingValues[1]:
    if decreasingValues[0] == decreasingValues[2]:
        print("TRIANGULO EQUILATERO")
    elif decreasingValues[0] != decreasingValues[2]:
        print("TRIANGULO ISOSCELES")
elif decreasingValues[0] == decreasingValues[2]:
    if decreasingValues[0] != decreasingValues[1]:
        print("TRIANGULO ISOSCELES")
elif decreasingValues[1] == decreasingValues[2]:
    if decreasingValues[1] != decreasingValues[0]:
        print("TRIANGULO ISOSCELES")
