# Read an integer N. This N will be the number of integer numbers X that will be read.

# Print how many these numbers X are in the interval [10,20] and how many values are out of this interval.
numbersIn = 0
numbersOut = 0
interval = [i for i in range(10,21)]
numbersList = []


try:
    totalOfNumbers = int(input(""))
    totalOfNumbers<10000

    for i in range(totalOfNumbers):
        n = int(input(""))
        if n > -10**7 and n<10**7:
            numbersList.append(n)
    for i in numbersList:
        if i in interval:
            numbersIn +=1
        else:
            numbersOut+=1

    print(f'''{numbersIn} in
{numbersOut} out''')

except:
    print("Number out of range.")