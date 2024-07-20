#Read 4 integer values A, B, C and D. 
# Then if B is greater than C and D is greater than A and if the sum of C and D is greater than the sum of A and B and if C and D were positives values and if A is even, write the message “Valores aceitos” (Accepted values). 
# Otherwise, write the message “Valores nao aceitos” (Values not accepted).

# B > C
# D > A 
# (C+D)>(A+B)
# C > 0
# D > 0
# A%2==0

valores = input()
valores = valores.split()
A = int(valores[0])
B = int(valores[1])
C = int(valores[2])
D = int(valores[3])

if B>C and D>A and (C+D)>(A+B) and C>0 and D>0 and A%2==0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")