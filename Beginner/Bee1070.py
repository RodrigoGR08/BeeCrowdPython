#Read an integer value X and print the 6 consecutive odd numbers from X, a value per line, including X if it is the case.

n = int(input(""))
oddcounter = 0
for i in range(n, n+100):
    if i%2!=0 and oddcounter<=5:
        print(i)
        oddcounter+=1
    else:
        pass