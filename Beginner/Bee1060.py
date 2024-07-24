#Write a program that reads 6 numbers. These numbers will only be positive or negative (disregard null values). Print the total number of positive numbers.

inputs = []
positiveCounter = 0
for i in range(6):
    linha = float(input())
    inputs.append(linha)

for num in inputs:
    if num>0:
        positiveCounter+=1

print(f'{positiveCounter} valores positivos')