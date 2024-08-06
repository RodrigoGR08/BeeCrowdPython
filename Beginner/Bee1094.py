# Maria has just started as graduate student in a medical school and she's needing your help to organize a laboratory experiment which she is responsible about. 
# She wants to know, at the end of the year, how many animals were used in this laboratory and the percentage of each type of animal is used at all.

# This laboratory uses in particular three types of animals: frogs, rats and rabbits. 
# To obtain this information, it knows exactly the number of experiments that were performed, the type and quantity of each animal is used in each experiment.

quantityOfTests = int(input(""))
tests = {}
totalTests = 0

totalRats = 0

totalFrogs = 0
frogsPercentage = 0

totalRabbits = 0
rabbitsPercentage = 0


for i in range(quantityOfTests):
    amount, animal = map(str, input().split())
    tests[i] = [int(amount), animal]

for amount, animal in tests.values():
    totalTests += amount
    if animal.upper() == "R":
        totalRats+=amount
    elif animal.upper() == "S":
        totalFrogs+=amount
    elif animal.upper() == "C":
        totalRabbits+=amount

ratsPercentage = totalRats/totalTests
frogsPercentage = totalFrogs/totalTests
rabbitsPercentage = totalRabbits/totalTests

print(f'''Total: {totalTests} cobaias
Total de coelhos: {totalRabbits}
Total de ratos: {totalRats}
Total de sapos: {totalFrogs}
Percentual de coelhos: {rabbitsPercentage*100:.2f} %
Percentual de ratos: {ratsPercentage*100:.2f} %
Percentual de sapos: {frogsPercentage*100:.2f} %''')

    