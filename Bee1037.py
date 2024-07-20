#You must make a program that read a float-point number and print a message saying in which of following intervals the number belongs: [0,25] (25,50], (50,75], (75,100]. 
# If the read number is less than zero or greather than 100, the program must print the message “Fora de intervalo” that means "Out of Interval".

firstInterval = 25.00
secondInterval = 50.00
thirdInterval = 75.00
fourthInterval = 100.00

n = float(input())
if n>=0 and n<=firstInterval:
    print("Intervalo [0,25]")
elif n>firstInterval and n<= secondInterval:
    print("Intervalo (25,50]")
elif n > secondInterval and n <= thirdInterval:
    print("Intervalo (50,75]")
elif n > thirdInterval and n <= fourthInterval:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")