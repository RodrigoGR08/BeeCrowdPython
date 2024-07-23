#Read two integer values (A and B). After, the program should print the message "Sao Multiplos" (are multiples) or "Nao sao Multiplos" (aren’t multiples), corresponding to the read values.
A, B = map(int, input().split())
if A%B==0 or B%A==0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

