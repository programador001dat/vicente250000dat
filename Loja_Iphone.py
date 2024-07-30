import os
import sys

script = '''Iphone PLusDigital'''
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(f"\tBem-vindo a nossa loja {script}")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

def MercadoriaEstoque():

    try:

        while True:

            MERCADORIA = {}
            MERCADORIA['apple_iphone'] = {'PRECO':'4550'}
            MERCADORIA['iphone_3g'] = {'PRECO':'3400'}
            MERCADORIA['iphone_3gs'] = {'PRECO':'5500'}
            MERCADORIA['iphone_4'] = {'PREÇO':'2800'}
            MERCADORIA['iphone_4_cdma'] = {'PRECO':'5000'}
            MERCADORIA['iphone_4s'] = {'PRECO':'2799'}
            MERCADORIA['iphone_5'] = {'PRECO':'2900'}
            MERCADORIA['iphone_5c'] = {'PRECO':'2700'}
            MERCADORIA['iphone_5s'] = {'PRECO':'2950'}
            MERCADORIA['iphone_6_plus'] = {'PRECO':'2500'}
            MERCADORIA['iphone_6s_plus'] = {'PRECO':'3550'}
            MERCADORIA['iphone_se'] = {'PRECO':'3500'}

            for a, b in MERCADORIA.items():
                print(f"{a}\t\t\t\t{b}")

            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            user = (str(input(">>ESCOLA COMPRAR IPHONE: ")))
            rece = user

            if rece in MERCADORIA or user is True:
                print(f"\t{rece} Ja está no carrinho.")
                MERCADORIA == rece
                print(MERCADORIA[rece],"\tPronto para pagar.")
                email = input(">>Informe o E-mail, o boleto sera enviado por lá:\t")
                recv = email
                with open("registro.txt", "w") as arquivo:
                    arquivo.write(recv)

            else:
                print("\tEspecifique o nome correto igual acima.")

    except Exception:
        print("\tAconteceu algo com o scripting.")


MercadoriaEstoque()
