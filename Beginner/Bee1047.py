#Read the start time and end time of a game, in hours and minutes (initial hour, initial minute, final hour, final minute). 
#Then print the duration of the game, knowing that the game can begin in a day and finish in another day,

#Obs.: With a maximum game time of 24 hours and the minimum game time of 1 minute.

horaInicial, minutoInicial, horaFinal, minutoFinal = map(int, input().split())

if horaInicial > horaFinal:
    duracaoHoras = (24 - horaInicial) + horaFinal
    if minutoInicial > minutoFinal:
        duracaoHoras-=1
        duracaoMinutos = (60 - minutoInicial) + minutoFinal
    elif minutoInicial == minutoFinal:
        duracaoMinutos = 0
    else:
        duracaoMinutos = minutoFinal - minutoInicial
elif horaInicial == horaFinal:
    duracaoHoras = 24
    if minutoInicial > minutoFinal:
        duracaoHoras-=1
        duracaoMinutos = (60 - minutoInicial) + minutoFinal
    elif minutoInicial == minutoFinal:
        duracaoMinutos = 0
    else:
        duracaoHoras = 0
        duracaoMinutos = minutoFinal - minutoInicial
else:
    duracaoHoras = horaFinal - horaInicial
    if minutoInicial > minutoFinal:
        duracaoHoras-=1
        duracaoMinutos = (60 - minutoInicial) + minutoFinal
    elif minutoInicial == minutoFinal:
        duracaoMinutos = 0
    else:
        duracaoMinutos = minutoFinal - minutoInicial
print(f'O JOGO DUROU {duracaoHoras:.0f} HORA(S) E {duracaoMinutos:.0f} MINUTO(S)')
