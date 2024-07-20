#Using the following table, write a program that reads a code and the amount of an item. After, print the value to pay. This is a very simple program with the only intention of practice of selection commands.
#Cachorro quente - R$4,00
#x - salada - R$4,50
#x -bacon - R$5,00
#Torrada simples - R$2,00
#Refrigerante - R$1,50

pedido, quantidade = map(int,input().split())
match pedido:
    case 1:
        print(f'Total: R$ {quantidade*4:.2f}')
    case 2:
        print(f'Total: R$ {quantidade*4.50:.2f}')
    case 3:
        print(f'Total: R$ {quantidade*5:.2f}')
    case 4:
        print(f'Total: R$ {quantidade*2:.2f}')
    case 5:
        print(f'Total: R$ {quantidade*1.5:.2f}')
    