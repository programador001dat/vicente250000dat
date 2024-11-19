import os
import time

os.system("clear")
passar_de_ano_nota_total = (5)
notas_aprovadas = []
notas_reprovadas = []

def SystemAdministratorSchool():

    while True:

        print("................................................................")
        print(".[0]visualizar notas")
        print(".[1]matematica")
        print(".[2]portugues")
        print(".[3]historia")
        print(".[4]ciencias")
        print(".[5]educacao fisica")
        print(".[6]artes")
        print(".[7]ingles")
        print("................................................................")

        professor = input("\n>>adicionar no em qual?: ")
        if professor == "1":
            print("\n\t\t\t|==> MATEMATICA <==|")
            n1 = int(input(f"Digite do 1ºbimestre: "))
            n2 = int(input(f"Digite do 2ºbimestre: "))
            n3 = int(input(f"Digite do 3ºbimestre: "))
            n4 = int(input(f"Digite do 4ºbimestre: "))
            print("................................................................")

            todas_as_notas = (n1+n2+n3+n4)
            rece = (todas_as_notas / 4)

            if rece >= passar_de_ano_nota_total:
                notas_aprovadas.append(rece)
                print("\n\t\t\t[+]aprovado")
                time.sleep(3)
                os.system("clear")

            elif rece <= passar_de_ano_nota_total:
                print("\n\t\t\t[+]reprovado")
                notas_reprovadas.append(rece)
                time.sleep(3)
                os.system("clear")

        elif professor == "2":
            print("\n\t\t\t|==> PORTUGUES <==|")
            n1 = int(input(f"Digite do 1ºbimestre: "))
            n2 = int(input(f"Digite do 2ºbimestre: "))
            n3 = int(input(f"Digite do 3ºbimestre: "))
            n4 = int(input(f"Digite do 4ºbimestre: "))
            print("................................................................")

            todas_as_notas = (n1+n2+n3+n4)
            rece = (todas_as_notas / 4)

            if rece >= passar_de_ano_nota_total:
                print("\n\t\t\t[+]aprovado")
                notas_aprovadas.append(rece)
                time.sleep(3)
                os.system("clear")

            elif rece <= passar_de_ano_nota_total:
                print("\n\t\t\t[+]reprovado")
                notas_reprovadas.append(rece)
                time.sleep(3)
                os.system("clear")

        elif professor == "3":
            print("\n\t\t\t|==> HISTORIA <==|")
            n1 = int(input(f"Digite do 1ºbimestre: "))
            n2 = int(input(f"Digite do 2ºbimestre: "))
            n3 = int(input(f"Digite do 3ºbimestre: "))
            n4 = int(input(f"Digite do 4ºbimestre: "))
            print("................................................................")

            todas_as_notas = (n1+n2+n3+n4)
            rece = (todas_as_notas / 4)

            if rece >= passar_de_ano_nota_total:
                print("\n\t\t\t[+]aprovado")
                notas_aprovadas.append(rece)
                time.sleep(3)
                os.system("clear")

            elif rece <= passar_de_ano_nota_total:
                print("\n\t\t\t[+]reprovado")
                notas_reprovadas.append(rece)
                time.sleep(3)
                os.system("clear")

        elif professor == "4":
            print("\n\t\t\t|==> CIENCIAS <==|")
            n1 = int(input(f"Digite do 1ºbimestre: "))
            n2 = int(input(f"Digite do 2ºbimestre: "))
            n3 = int(input(f"Digite do 3ºbimestre: "))
            n4 = int(input(f"Digite do 4ºbimestre: "))
            print("................................................................")

            todas_as_notas = (n1+n2+n3+n4)
            rece = (todas_as_notas / 4)

            if rece >= passar_de_ano_nota_total:
                print("\n\t\t\t[+]aprovado")
                notas_aprovadas.append(rece)
                time.sleep(3)
                os.system("clear")

            elif rece <= passar_de_ano_nota_total:
                print("\n\t\t\t[+]reprovado")
                notas_reprovadas.append(rece)
                time.sleep(3)
                os.system("clear")

        elif professor == "5":
            print("\n\t\t\t|==> EDUCACAO FISICA <==|")
            n1 = int(input(f"Digite do 1ºbimestre: "))
            n2 = int(input(f"Digite do 2ºbimestre: "))
            n3 = int(input(f"Digite do 3ºbimestre: "))
            n4 = int(input(f"Digite do 4ºbimestre: "))
            print("................................................................")

            todas_as_notas = (n1+n2+n3+n4)
            rece = (todas_as_notas / 4)

            if rece >= passar_de_ano_nota_total:
                print("\n\t\t\t[+]aprovado")
                notas_aprovadas.append(rece)
                time.sleep(3)
                os.system("clear")

            elif rece <= passar_de_ano_nota_total:
                print("\n\t\t\t[+]reprovado")
                notas_reprovadas.append(rece)
                time.sleep(3)
                os.system("clear")

        elif professor == "6":
            print("\n\t\t\t|==> ARTES <==|")
            n1 = int(input(f"Digite do 1ºbimestre: "))
            n2 = int(input(f"Digite do 2ºbimestre: "))
            n3 = int(input(f"Digite do 3ºbimestre: "))
            n4 = int(input(f"Digite do 4ºbimestre: "))
            print("................................................................")

            todas_as_notas = (n1+n2+n3+n4)
            rece = (todas_as_notas / 4)

            if rece >= passar_de_ano_nota_total:
                print("\n\t\t\t[+]aprovado")
                notas_aprovadas.append(rece)
                time.sleep(3)
                os.system("clear")

            elif rece <= passar_de_ano_nota_total:
                print("\n\t\t\t[+]reprovado")
                notas_reprovadas.append(rece)
                time.sleep(3)
                os.system("clear")

        elif professor == "7":
            print("\n\t\t\t|==> INGLES <==|")
            n1 = int(input(f"Digite do 1ºbimestre: "))
            n2 = int(input(f"Digite do 2ºbimestre: "))
            n3 = int(input(f"Digite do 3ºbimestre: "))
            n4 = int(input(f"Digite do 4ºbimestre: "))
            print("................................................................")

            todas_as_notas = (n1+n2+n3+n4)
            rece = (todas_as_notas / 4)

            if rece >= passar_de_ano_nota_total:
                print("\n\t\t\t[+]aprovado")
                notas_aprovadas.append(rece)
                time.sleep(3)
                os.system("clear")

            elif rece <= passar_de_ano_nota_total:
                print("\n\t\t\t[+]reprovado")
                notas_reprovadas.append(rece)
                time.sleep(3)
                os.system("clear")

        elif professor == "0":
            print("................................................................")
            print(f"[+]notas aprovadas: {notas_aprovadas}\n")
            print(f"[+]notas reprovadas: {notas_reprovadas}\n")

        else:
            print(">>operacao invalida reinicie o programa.")
            quit()



SystemAdministratorSchool()