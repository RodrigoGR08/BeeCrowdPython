#Make a program that reads five integer values. Count how many of these values ​​are even and  print this information like the following example.

values = []
evenValues = []
for i in range(5):
    values.append(int(input()))

for value in values:
    if value%2==0:
        evenValues.append(value)
    
print(f'{len(evenValues)} valores pares')