import random

def Root():
    return random.randing(1,100)

def Gamer():
    password = (145)
    rounds = 3
    chute = 0

    while chute is not password:
        rounds +=1
        chute = int(input("\n DIGITE O CODIGO DE 2 DIGITOS: "))
        
        if chute > password:
            print("\n Longe demais. -",chute)
            
        elif chute < password:
            print("\n Passou perto. +",chute)
            
        else:
            print("\n Parebéns. Ganhou 10Flags.", )
            break

Gamer()
