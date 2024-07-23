# Read the start time and end time of a game, in hours.
# Then calculate the duration of the game, knowing that the game can begin in a day and finish in another day, with a maximum duration of 24 hours.
# The message must be printed in portuguese “O JOGO DUROU X HORA(S)” that means “THE GAME LASTED X HOUR(S)”
tempoInicial, tempoFinal = map(int, input().split())

if tempoInicial > tempoFinal:
    duracao = (24 - tempoInicial) + tempoFinal
elif tempoInicial == tempoFinal:
    duracao = 24
else:
    duracao = tempoFinal - tempoInicial
print(f'O JOGO DUROU {duracao:.0f} HORA(S)')
