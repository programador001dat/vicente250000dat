import time
import sys
import os
from asyncio import timeout



def __main__():
    c = ("----------------------------------------")
    s = ("[#]         SQL Lanchonete.py        [#]")
    d = ("----------------------------------------")
    print("\n",c,"\n",s,"\n",d,"\n")



__main__()


class LanchoneteScript():

    def RetiradaPedidos(cardapio):
        cardapio = ['x-burguer', 'x-cachorro-quente', 'x-salada', 'x-calabreza','x-tudo','x-bacon','pizza-calabreza','pizza-4-queijo','pizza-presuntao','pizza-frango']
        for i in cardapio:
            print("|",i)

        user = input("\n==>LANCHE PRONTO?\t==> ")
        go = user
        if go in cardapio or go is True:
            print(go,"\tPRONTO PARA ENTREGA\n")

        else:
            print("\tNão LOCALIZADO NA LISTA")
            quit()



    RetiradaPedidos(cardapio="user")


    motoboy = ['caio','joao']
    msg = ("[#]Motoboy disponivel")
    print(f"==>{msg}")
    for i in motoboy:
        print(f"A espera.............................. {i}")



    def Entregador(motoboy,RetiradaPedidos):

        boy = input("\n\nMotoboy==> caio\t\tMotoboy==> joao\nDIGITE ==>: ")
        rece = str(boy)

        if rece in motoboy or rece is True:
            print(f"{rece} está pronto(!)")

        elif boy == "caio":

            print(f"\n{rece} Motoboy saiu no percurso.\n")
            time.sleep(2)
            print(".?")
            time.sleep(1)
            print("..?")
            time.sleep(2)
            print("...?")
            time.sleep(1)
            print("....?")
            time.sleep(2)
            print(".....?")
            time.sleep(1)
            print("......?")
            time.sleep(2)
            print(f"\n[OK] {rece} Entregador concluiu percurso!\n\n")

        elif boy == "joao":

            print(f"\n[OK] {rece} Motoboy saiu no percurso.\n")
            time.sleep(2)
            print(".?")
            time.sleep(1)
            print("..?")
            time.sleep(2)
            print("...?")
            time.sleep(1)
            print("....?")
            time.sleep(2)
            print(".....?")
            time.sleep(1)
            print("......?")
            time.sleep(2)
            print(f"\n [OK] {rece} Entregador concluiu percurso!\n\n")

        else:
            print("Nao localizado")



    Entregador(motoboy=[""],RetiradaPedidos=["user"])

    while True:

        re = input("Acess | Menu > Enter. ")
        if re == '':
            RetiradaPedidos(cardapio="user")

        de = input("Acess | Motoboy >Enter.")
        if de == '':
            Entregador(motoboy=[""],RetiradaPedidos=["user"])



LanchoneteScript()
