#Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.
segundosInicial = int(input())
segundos = segundosInicial
denominacoes = [3600, 60, 1]
finalTime = [0] * len(denominacoes)

for i, denom in enumerate(denominacoes):
    while segundos >= denom:
        segundos -= denom
        finalTime[i] += 1

print(f'{finalTime[0]}:{finalTime[1]}:{finalTime[2]}')