#Read two integer values X and Y. Print the sum of all odd values between them.

n1 = int(input(""))
n2 = int(input(""))
oddNumbers=[]

if n1>n2:
    for i in range(n2+1, n1):
        if i%2!=0:
            oddNumbers.append(i)
        else:
            pass
elif n2>n1:
    for i in range(n1+1, n2):
        if i%2!=0:
            oddNumbers.append(i)
        else:
            pass

print(sum(oddNumbers))