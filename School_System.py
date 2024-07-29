import os
import sys
###############################################################
# Script de calcular 4Bimestre e dividir pela nota da materia.
# Script sistema escolar. Passo de ano, Sim ou Nao.
# Script faz calculos de numeros Int e retornara numeros Int.
###############################################################
school = ('E.E. Plinio Rodrigues de Moraes.')
print(f"{school}")
nome_aluno = (str(input(">>Nome do Aluno:\t")))
serie_aluno = (str(input(">>Serie do Aluno:\t")))
aluno = nome_aluno
serie = serie_aluno
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(f">> Aluno: {aluno}\tSerie: {serie}")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

try:


    while True:


        def Matematica():


            print("\tMateria: MATEMÁTICA")
            materia = 'Matematica'
            matematica = 6
            bimestre_one = (int(input(" Nota do primeiro 1°bimestre:\t")))
            NotaOne = (int(bimestre_one))
            bimestre_two = (int(input(" Nota do primeiro 2°bimestre:\t")))
            NotaTwo = (int(bimestre_two))
            bimestre_three = (int(input(" Nota do primeiro 3°bimestre:\t")))
            NotaThree = (int(bimestre_three))
            bimestre_four = (int(input(" Nota do primeiro 4°bimestre:\t")))
            NotaFour = (int(bimestre_four))

            dados = (float(NotaOne + NotaTwo + NotaThree + NotaFour))/4

            if dados >= matematica:
                print(f"\tNota final: {dados}<-->\t{aluno}\tPASSOU {materia}\n")

            elif dados <= matematica:
                print(f">>{aluno}\tREPETIU {materia}\n")

            else:
                print("\tAlgo de errado?")


        Matematica()

        def Portugues():

            print("\tMateria: LINGUA-PORTUGUESA")
            materia = 'Portugues'
            portugues = 6
            bimestre_one = (int(input(" Nota do primeiro 1°bimestre:\t")))
            NotaOne = (int(bimestre_one))
            bimestre_two = (int(input(" Nota do primeiro 2°bimestre:\t")))
            NotaTwo = (int(bimestre_two))
            bimestre_three = (int(input(" Nota do primeiro 3°bimestre:\t")))
            NotaThree = (int(bimestre_three))
            bimestre_four = (int(input(" Nota do primeiro 4°bimestre:\t")))
            NotaFour = (int(bimestre_four))

            dados = (float(NotaOne + NotaTwo + NotaThree + NotaFour))/4

            if dados >= portugues:
                print(f"\tNota final: {dados}<-->\t{aluno}\tPASSOU {materia}\n")

            elif dados <= portugues:
                print(f">>{aluno}\tREPETIU {materia}\n")

            else:
                print("\tAlgo de errado?")


        Portugues()

        def Ciencias():

            print("\tMateria: CIÊNCIAS")
            materia = 'Ciencia'
            ciencias = 6
            bimestre_one = (int(input(" Nota do primeiro 1°bimestre:\t")))
            NotaOne = (int(bimestre_one))
            bimestre_two = (int(input(" Nota do primeiro 2°bimestre:\t")))
            NotaTwo = (int(bimestre_two))
            bimestre_three = (int(input(" Nota do primeiro 3°bimestre:\t")))
            NotaThree = (int(bimestre_three))
            bimestre_four = (int(input(" Nota do primeiro 4°bimestre:\t")))
            NotaFour = (int(bimestre_four))

            dados = (float(NotaOne + NotaTwo + NotaThree + NotaFour)) / 4

            if dados >= ciencias:
                print(f"\tNota final: {dados}<-->\t{aluno}\tPASSOU {materia}\n")

            elif dados <= ciencias:
                print(f">>{aluno}\tREPETIU {materia}\n")

            else:
                print("\tAlgo de errado?")


        Ciencias()
        def Ingles():

            print("\tMateria: INGLÊS")
            materia = 'Ingles'
            ingles = 6
            bimestre_one = (int(input(" Nota do primeiro 1°bimestre:\t")))
            NotaOne = (int(bimestre_one))
            bimestre_two = (int(input(" Nota do primeiro 2°bimestre:\t")))
            NotaTwo = (int(bimestre_two))
            bimestre_three = (int(input(" Nota do primeiro 3°bimestre:\t")))
            NotaThree = (int(bimestre_three))
            bimestre_four = (int(input(" Nota do primeiro 4°bimestre:\t")))
            NotaFour = (int(bimestre_four))

            dados = (float(NotaOne + NotaTwo + NotaThree + NotaFour)) / 4

            if dados >= ingles:
                print(f"\tNota final: {dados}<-->\t{aluno}\tPASSOU {materia}\n")

            elif dados <= ingles:
                print(f">>{aluno}\tREPETIU {materia}\n")

            else:
                print("\tAlgo de errado?")


        Ingles()
        def Historia():

            print("\tMateria: HISTÔRIA")
            materia = 'Historia'
            historia = 6
            bimestre_one = (int(input(" Nota do primeiro 1°bimestre:\t")))
            NotaOne = (int(bimestre_one))
            bimestre_two = (int(input(" Nota do primeiro 2°bimestre:\t")))
            NotaTwo = (int(bimestre_two))
            bimestre_three = (int(input(" Nota do primeiro 3°bimestre:\t")))
            NotaThree = (int(bimestre_three))
            bimestre_four = (int(input(" Nota do primeiro 4°bimestre:\t")))
            NotaFour = (int(bimestre_four))

            dados = (float(NotaOne + NotaTwo + NotaThree + NotaFour)) / 4

            if dados >= historia:
                print(f"\tNota final: {dados}<-->\t{aluno}\tPASSOU {materia}\n")

            elif dados <= historia:
                print(f">>{aluno}\tREPETIU {materia}\n")

            else:
                print("\tAlgo de errado?")


        Historia()
        def Artes():

            print("\tMateria: ARTES")
            materia = 'Artes'
            artes = 6
            bimestre_one = (int(input(" Nota do primeiro 1°bimestre:\t")))
            NotaOne = (int(bimestre_one))
            bimestre_two = (int(input(" Nota do primeiro 2°bimestre:\t")))
            NotaTwo = (int(bimestre_two))
            bimestre_three = (int(input(" Nota do primeiro 3°bimestre:\t")))
            NotaThree = (int(bimestre_three))
            bimestre_four = (int(input(" Nota do primeiro 4°bimestre:\t")))
            NotaFour = (int(bimestre_four))

            dados = (float(NotaOne + NotaTwo + NotaThree + NotaFour)) / 4

            if dados >= artes:
                print(f"\tNota final: {dados}<-->\t{aluno}\tPASSOU {materia}\n")

            elif dados <= artes:
                print(f">>{aluno}\tREPETIU {materia}\n")

            else:
                print("\tAlgo de errado?")


        Artes()
        def EdFisica():

            print("\tMateria: CIÊNCIAS")
            materia = 'Educacao Fisica'
            edfisica = 6
            bimestre_one = (int(input(" Nota do primeiro 1°bimestre:\t")))
            NotaOne = (int(bimestre_one))
            bimestre_two = (int(input(" Nota do primeiro 2°bimestre:\t")))
            NotaTwo = (int(bimestre_two))
            bimestre_three = (int(input(" Nota do primeiro 3°bimestre:\t")))
            NotaThree = (int(bimestre_three))
            bimestre_four = (int(input(" Nota do primeiro 4°bimestre:\t")))
            NotaFour = (int(bimestre_four))

            dados = (float(NotaOne + NotaTwo + NotaThree + NotaFour)) / 4

            if dados >= edfisica:
                print(f"\tNota final: {dados}<-->\t{aluno}\tPASSOU {materia}\n")

            elif dados <= edfisica:
                print(f">>{aluno}\tREPETIU {materia}\n")

            else:
                print("\tAlgo de errado?")


        EdFisica()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")


except Exception:
    print("\tDigite numeros para fazer os calculos.")