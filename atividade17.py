#Exercício Python 17: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata
# de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.
anodenasc = float(input("qual o ano uq você nasceu?"))
anotual = float(input("qual o ano atual?"))
idade = anotual - anodenasc
if idade>18 :
    print("já passou do tempo do alistamento.")
elif idade==18:
    print(" é a hora exata de se alistar")
elif idade<18:
        tempo=idade-18
        print("não está no momento de se alistar")
        print(f'falta {tempo} anos para você se alistar')


