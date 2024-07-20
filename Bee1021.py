#Read a value of floating point with two decimal places. This represents a monetary value. 
# After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. 
# The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. 
# Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.
valorInicial = float(input())
if valorInicial >= 0 and valorInicial <= 1000000.00:
    valortotal = valorInicial*100
    denominacoes = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
    quantidades = [0] * len(denominacoes)
    indexDeSperacao = denominacoes.index(100)
    for i, denom in enumerate(denominacoes):
        valortotal = round(valortotal, 3)
        while  valortotal >= denom:
            valortotal -= denom
            quantidades[i]+=1
    print("NOTAS:")
    for quantidade, valor in zip(quantidades[:indexDeSperacao], denominacoes[:indexDeSperacao]):
        print(f'{quantidade} nota(s) de R$ {valor/100:.2f}')
    print("MOEDAS:")
    for quantidade, valor in zip(quantidades[indexDeSperacao:], denominacoes[indexDeSperacao:]):
        print(f'{quantidade} moeda(s) de R$ {valor/100:.2f}')
else:
    pass
