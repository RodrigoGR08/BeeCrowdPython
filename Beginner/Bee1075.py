#Read an integer N. Print all numbers between 1 and 10000, which divided by N will give the rest = 2.

value = int(input())

if value <10000:
    for i in range(10000+1):
        if i%value==2:
            print(i)