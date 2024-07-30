#Make a program that reads five integer values. 
# Count how many   of these values are even, odd, positive and negative. 
# Print these information like following example.

values = []
evenList = []
oddList = []
positiveList = []
negativeList = []
for i in range(5):
    values.append(int(input()))

#Methods
def checkPositeNumber(n):
    if n > 0:
        positiveList.append(n)
    
def checkNegativeNumber(n):
    if n<0:
        negativeList.append(n)

def checkOddNumber(n):
    if n%2!=0:
        oddList.append(n)

def checkEvenNumber(n):
    if n%2==0:
        evenList.append(n)



for value in values:
    checkPositeNumber(value)
    checkNegativeNumber(value)
    checkOddNumber(value)
    checkEvenNumber(value)


print(f'''{len(evenList)} valor(es) par(es)
{len(oddList)} valor(es) impar(es)
{len(positiveList)} valor(es) positivo(s)
{len(negativeList)} valor(es) negativo(s)''')

