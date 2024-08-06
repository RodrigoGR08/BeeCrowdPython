#Read an integer N. 
# Print the square of each one of the even values from 1 to N including N if it is the case.

n = int(input(""))

if n >5 and n < 2000:
    for i in range(1,n+1):
        if i%2==0:
            print(f'{i}^2 = {i**2}')
        else:
            pass