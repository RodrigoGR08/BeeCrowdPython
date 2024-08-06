#Read an integer value N. 
# After, read these N values and print a message for each value saying if this value is odd, even, positive or negative. 
# In case of zero (0), although the correct description would be "EVEN NULL", because by definition zero is even, your program must print only "NULL", without quotes.

values = []
quantityOfNumbers = int(input())

if quantityOfNumbers < 10000:
    for i in range(quantityOfNumbers):
        value = int(input())
        if value > -(10)**7 and value < 10**7:
            values.append(value)
    for value in values:
        if value<0:
            if value%2==0:
                print("EVEN NEGATIVE")
            else:
                print("ODD NEGATIVE")
        elif value==0:
            print("NULL")
        else:
            if value%2==0:
                print("EVEN POSITIVE")
            else:
                print("ODD POSITIVE")
        
    
