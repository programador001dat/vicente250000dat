import os
import time
import random

os.system("clear")

print("\t___________________")
print("\t| ............... |\t\tIfood Entregador.")
print("\t| |             | |]\t\tFique online para receber pedidos.")
print("\t| |   Ifood.py  | |\t\tGanhe dinheiro com nosso APP.")
print("\t| | Entregador  | |)\t\tEntre em contato com nosso suporte.")
print("\t| |_____________| |)\t\tPara mais informações.")
print("\t|_________________|\t\tacesse www.ifood.com")
print("\t|______|OFF|______|")
print("\t|  abc  def  ghi  |")
print("\t|  jkl  mno  pqrs |")
print("\t|    tuv wxyz     |")
print("\t|_________________|\n")

restaurantes = ["Cirineu Lanches","Edson Lanches","Grilleto Tauste","Tammy Pastelaria","Pana","O Botequim da Francisca","Oca Burguer","Cali Burguer","Mansour","Panella Express","Alemão Burguer","Haw Braws","Homburguer","MC Donaldo","Burguer King","Bolos da Elda","Encontro com Doces"]
valores_a_pagar = ["6.50","7.14","7.00","8.20","9.00","10.59","11.49","12.50","13.00","14.50","15.00","16.90","17.20","8.50","9.12","10.10","11.00"]
endereco = ["Jardim Europa","vila lucy","vila indenpendencia","vila leao","jardim simus","Av. sao paulo","Dr. americo frigueredo","Av. armando pannunzio","Av. antonio carlos comitre","vila barao","Av. Barão de Tatuí","Vila Jardine"]
rua = ["R. francisco de queiroz","R. da penha","Dr. americo figueredo","Av. armando pannunzio","Av. sao paulo","Av. antonio carlos comitre","R.sete de setembro","R. vinte oito de outubro","R. mileto de morais","R. são luiz bernado"]
numero = ["90","3220","125","70","120","80","192","220","300","1239","56","890","490","19"]
km = ["2km","3km","4km","5km","10km","900m","12km","15km"]

def MotoboyInicia():

    disponivel = input(">> deseja ficar disponivel Y/n: ")

    if disponivel == "y":

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[+]online.")
        print("..............................................................................")
        print("\t\t\t       ................")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|  Disponivel  |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("\t\t\t       ................\n..............................................................................\n\n")

        time.sleep(3)

        x = random.choice(restaurantes)
        y = random.choice(valores_a_pagar)
        k = random.choice(km)

        print(f"\t\tIfood {x} valor {y}$ KM: {k}")

        coletar_rota = input("\t\t\t[y]aceitar or [n]rejeitar \n\t\t\t\t>>: ")

        if coletar_rota == "y":




            print("\n\n\n\n\n$\t$\t$\t$\t$\t$\t$\t$\t$\t$\t$\t")
            time.sleep(2)

            print("\n[+]pesquisando a rota.\n")
            time.sleep(3)

            print("[+]pesquisando a rota..\n")
            time.sleep(4)

            print("[+]pesquisando a rota...")
            os.system("clear")

            e = random.choice(endereco)
            r = random.choice(rua)
            n = random.choice(numero)

            os.system("clear")
            print(":::::::::::::::::::::::> Informacoes do restaurante <:::::::::::::::::::::::\n")
            print(f"|Restaurante: {x}\n|Endereço: {e}\n|Complemento: {r} {n}\n..............................................................................")


        else:
            print("\n\n\n\n\n\n\n\nX\tX\tX\tX\tX\tX\tX\tX\tX\tX\tX\t\n")
            print("\t\t\t  >> rejeitamos a rota <<\n")
            print("X\tX\tX\tX\tX\tX\tX\tX\tX\tX\tX\t\n\n\n\n\n")


            time.sleep(4)
            os.system("clear")

            print("\n\n\n\n\n\n\n\n\n\n\n\n[+]online.")
            print("..............................................................................")
            print("\t\t\t       ................")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|  Disponivel  |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("\t\t\t       ................\n..............................................................................\n\n")


            x = random.choice(restaurantes)
            y = random.choice(valores_a_pagar)

            time.sleep(4)
            print(f"\t\tIfood {x} valor {y}$ KM: {k}")

            coletar_rota = input("\t\t\t[y]aceitar or [n]rejeitar \n\t\t\t\t>>: ")

            if coletar_rota == "y":
                print("\n\n\n\n\n$\t$\t$\t$\t$\t$\t$\t$\t$\t$\t$\t")
                time.sleep(2)

                print("\n[+]pesquisando a rota.\n")
                time.sleep(3)

                print("[+]pesquisando a rota..\n")
                time.sleep(4)

                print("[+]pesquisando a rota...")
                os.system("clear")

                e = random.choice(endereco)
                r = random.choice(rua)
                n = random.choice(numero)
                os.system("clear")

                print(":::::::::::::::::::::::> Informacoes do restaurante <:::::::::::::::::::::::\n")
                print(f"|Restaurante: {x}\n|Endereço: {e}\n|Complemento: {r} {n}\n..............................................................................")

            elif coletar_rota == "n":
                print("\nX\tX\tX\tX\tX\tX\tX\tX\tX\tX\tX\t\n")
                print("\t\t\t\t >> rejeitamos muitas rotas <<\n")
                print("X\tX\tX\tX\tX\tX\tX\tX\tX\tX\tX\t\n\n\n\n\n")
                print("\n>>Foi desconectado no app.")




    else:
        print("[*]offline")


MotoboyInicia()
