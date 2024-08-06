# Read an integer N (2 < N < 1000). Print the multiplication table of N.
# 1 x N = N      2 x N = 2N        ...       10 x N = 10N  

number = int(input(""))
if number>1 and number<1000:
    for i in range(1,11):
        print(f'{i} x {number} = {number*i}')