day, startDate = input("").split()
startDate = int(startDate)
horaInicial, minutoInicial, segundoInicial  = map(int, input().split(":"))

day, endingDate = input("").split()
endingDate = int(endingDate)
horaFinal, minutoFinal, segundoFinal = map(int, input().split(":"))

totalSeconds = segundoFinal - segundoInicial
totalMinutes = minutoFinal - minutoInicial
totalHours = horaFinal - horaInicial
totalDays = endingDate - startDate

if(totalSeconds<0):
    totalSeconds+=60
    totalMinutes-=1


if(totalMinutes<0):
    totalMinutes+=60
    totalHours-=1


if(totalHours<0):
    totalHours+=24
    totalDays-=1


print(f'''{totalDays} dia(s)
{totalHours} hora(s)
{totalMinutes} minuto(s)
{totalSeconds} segundo(s)''')