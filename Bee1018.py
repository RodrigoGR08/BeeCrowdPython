#In this problem you have to read an integer value and calculate the smallest possible number of banknotes in which the value may be decomposed. The possible banknotes are 100, 50, 20, 10, 5, 2 and 1. Print the read value and the list of banknotes.
valorInicial = int(input())
valor = valorInicial
contadorDeNotasDeCem = 0
contadorDeNotasDeCinquenta = 0
contadorDeNotasDeVinte = 0
contadorDeNotasDeDez = 0
contadorDeNotasDeCinco = 0
contadorDeNotasDeDois = 0
contadorDeNotasDeUm = 0
while True:
    if valor >= 100:
        valor -= 100
        contadorDeNotasDeCem+=1
    elif valor <100 and valor >= 50:
        valor -= 50
        contadorDeNotasDeCinquenta+=1
    elif valor <50 and valor >= 20:
        valor -= 20
        contadorDeNotasDeVinte+=1
    elif valor <20 and valor >= 10:
        valor -= 10
        contadorDeNotasDeDez+=1
    elif valor <10 and valor >= 5:
        valor -=5
        contadorDeNotasDeCinco+=1
    elif valor <5 and valor >= 2:
        valor -= 2
        contadorDeNotasDeDois+=1
    elif valor<2 and valor>=1:
        valor -=1
        contadorDeNotasDeUm+=1
    else:
        break
print(f'''{valorInicial}
{contadorDeNotasDeCem} nota(s) de R$ 100,00
{contadorDeNotasDeCinquenta} nota(s) de R$ 50,00
{contadorDeNotasDeVinte} nota(s) de R$ 20,00
{contadorDeNotasDeDez} nota(s) de R$ 10,00
{contadorDeNotasDeCinco} nota(s) de R$ 5,00
{contadorDeNotasDeDois} nota(s) de R$ 2,00
{contadorDeNotasDeUm} nota(s) de R$ 1,00''')

