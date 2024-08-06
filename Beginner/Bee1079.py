#Weighted Averages

# Read an integer N, which represents the number of following test cases. 
# Each test case consists of three floating-point numbers, each one with one digit after the decimal point. 
# Print the weighted average for each of these sets of three numbers, considering that the first number has weight 2, the second number has weight 3 and the third number has weight 5.

quantityOfTests = int(input())
avgs = []

for i in range(quantityOfTests):
    n1, n2, n3 = map(float, input("").split())
    avg = ((n1*2)+(n2*3)+(n3*5))/(2+3+5)
    avgs.append(avg)
for element in avgs:
    print(f'{element:.1f}')