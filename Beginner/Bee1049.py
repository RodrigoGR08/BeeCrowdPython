#In this problem, your job is to read three Portuguese words. These words define an animal according to the table below, from left to right. After, print the chosen animal defined by these three words.
inputs = []
for i in range(3):
    linha = input()
    inputs.append(linha)

if inputs[0].capitalize() == "Vertebrado":
    if inputs[1].capitalize() == "Ave":
        if inputs[2].capitalize() == "Carnivoro":
            print("aguia")
        elif inputs[2].capitalize() == "Onivoro":
            print("pomba")
    elif inputs[1].capitalize() == "Mamifero":
        if inputs[2].capitalize() == "Onivoro":
            print("homem")
        elif inputs[2].capitalize() == "Herbivoro":
            print("vaca")
elif inputs[0].capitalize() == "Invertebrado":
    if inputs[1].capitalize() == "Inseto":
        if inputs[2].capitalize() == "Hematofago":
            print("pulga")
        elif inputs[2].capitalize() == "Herbivoro":
            print("lagarta")
    elif inputs[1].capitalize() == "Anelideo":
        if inputs[2].capitalize() == "Hematofago":
            print("sanguessuga")
        elif inputs[2].capitalize() == "Onivoro":
            print("minhoca")