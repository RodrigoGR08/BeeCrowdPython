inputs = []

for i in range(4):
    linha = input()
    inputs.append(linha)

diaInicial = int(inputs[0][-1])
horarioInicial = inputs[1].split(" : ")
print(horarioInicial)
for i in horarioInicial:
    horarioInicial[i] = int(horarioInicial[i])
print(horarioInicial)
horaInicial = int(horarioInicial[0])
minutosInicial, segundoInicial = int(inputs[1].split(" : "))
diaFinal = int(inputs[2][-1])
horaFinal, minutosFinal, segundoFinal = int(inputs[-1].split(" : "))


totalDias = diaFinal-diaInicial
#Hours
if horaFinal < int(horarioInicial[0]):
    totalDias-=1
    totalHoras = (24-horaFinal) + horaInicial
elif horaFinal == horaInicial:
    totalHoras = 0
else:
    totalHoras = horaFinal-horaInicial
#Minutes
if minutosFinal < minutosInicial:
    totalHoras-=1

    totalMinutos = (60-minutosFinal) + minutosInicial
elif minutosFinal == minutosInicial:
    totalMinutos = 0
else:
    totalMinutos = minutosFinal-minutosInicial
#Seconds
if segundoFinal < segundoInicial:
    totalMinutos-=1
    totalSegundo = (60-segundoFinal) + segundoInicial
elif segundoFinal == segundoInicial:
    totalSegundo = 0
else:
    totalSegundo = segundoFinal-segundoInicial

print(f'''{totalDias} dia(s)
      {totalHoras} hora(s)
      {totalMinutos} minuto(s)
      {totalSegundo} segundo(s)''')