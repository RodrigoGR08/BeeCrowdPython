#Read three integers and sort them in ascending order. After, print these values in ascending order, a blank line and then the values in the sequence as they were readed.
def breakLine():
    print("\n")
n1, n2, n3 = map(int, input().split())
numbers = [n1, n2, n3]
sortedNumbers = numbers[:]
for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        if sortedNumbers[i] > sortedNumbers[j]:
            sortedNumbers[i], sortedNumbers[j] = sortedNumbers[j], sortedNumbers[i]
    
for num in sortedNumbers:
    print(num)
print()
for num in numbers:
    print(num)

