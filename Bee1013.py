#Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". Use the following formula:
valores = input()
valores = valores.split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
MaiorAB = (a+b+abs(a-b))/2
MaiorFinal = (MaiorAB+c+abs(MaiorAB-c))/2
print(f'{MaiorFinal:.0f} eh o maior')