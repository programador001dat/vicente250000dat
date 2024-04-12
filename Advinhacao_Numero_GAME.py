import random
print('[?]Jogo de advinhação: acerte o codigo de 1 digitos\n')

def Jogo_advinhacao():
    return random.randing(1,100)

def Game():
    codigo = (5)
    tentativa = 5
    print('De 1 a 10')

    chute=0
    while chute is not codigo:
        tentativa +=1
        chute = int(input(' Digite o codigo _->'))
        if chute > codigo:
            print(' [+]Numemero alto...',chute)
        elif chute < codigo:
            print('[-]Numero baixo...',chute)
        else:
           print('_Acerto!\n', \
                tentativa,'<-Tentaivas')

Game()
