from random import randint
numero= randint(1,50)
for n in range(6):
    numero_digitado= int(input("digite um numero"))
    if numero_digitado > numero:
        print("menor")
    elif numero_digitado < numero:
        print("maior")
    else:
        print("numero digitado esta certo")
        tentativas=n+1
        print("você acertou com",tentativas)
        break




