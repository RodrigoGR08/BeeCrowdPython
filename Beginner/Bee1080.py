#Read 100 integer numbers. Print the highest read value and the input position.

highest = -99999999
position = 0

for i in range(1,101):
    number = int(input())
    if number > highest:
        highest = number
        position = i

print(highest)
print(position)