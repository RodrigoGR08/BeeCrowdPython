#Read an integer value X (1 <= X <= 1000).  Then print the odd numbers from 1 to X, each one in a line, including X if is the case.
oddValues = []
n = int(input())

for i in range(1, n+1):
    if i%2!=0:
        oddValues.append(i)

for value in oddValues:
    print(value)
