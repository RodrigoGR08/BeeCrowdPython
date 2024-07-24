# Read an integer number that is the code number for phone dialing. Then, print the destination according to the following table:




# If the input number isn’t found in the above table, the output must be:
# DDD nao cadastrado
# That means “DDD not found” in Portuguese language.

dDDDict = {61 : "Brasilia",
           71 : "Salvador",
           11 : "Sao Paulo",
           21 : "Rio de Janeiro",
           32 : "Juiz de Fora",
           19 : "Campinas",
           27 : "Vitoria",
           31 : "Belo Horizonte"}

n = int(input(""))
if n in dDDDict:
    print(dDDDict[n])