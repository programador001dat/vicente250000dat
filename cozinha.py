import os
import sys
import calendar

lista_semanas = {}
a = 2024
m = 7
print(calendar.month(a,m))
# Script de consultar um dicionario de chaves e valores.
# Script pega a string Opcao do usuario.
# Script faz, ve se tem a string no lista_semana.dict, depois faz comparacao com a string opcao do usuario.
# Script retorna valor verdadeiro ao do == dicionario, abrindo a lista de valor e print
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>                   CARDAPIO.py                 >>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(" Exemplo >>Semana: segunda\n\n")

lista_semanas['domingo'] = {'Arroz-Carreteiro, Feijoada, Farofa. (Alface com Tomate)/(Suco natural Laranja).'}
lista_semanas['segunda'] = {'Arroz-Branco, Feijao, Parmejeana. (Vinagrete)/(Suco natural Abacaxi).'}
lista_semanas['terca'] = {'Arroz-Branco, Feijao, macarrao com salsicha. (Vinagrete)/(Suco natural Laranja).'}
lista_semanas['quarta'] = {'Arroz-Branco, Feijao, Macarrao com Ovos Cozidos. (Suco natural Abacaixi).'}
lista_semanas['quinta'] = {'Arroz-Carreteiro, Feijoada, Farofa. (Suco natural Laranja).'}
lista_semanas['sexta'] = {'Arroz-Branco, Feijao, Pernil de Porco. (Suco natural Abacaixi).'}
lista_semanas['sabado'] = {'Arroz-Branco, Feijao, Macarrao com salsicha. (Suco natural Laranja).'}

try:


    while True:

        for i in lista_semanas:
            opcao = (str(input(">>Semana: ")))
            rece = str(opcao)

            if rece in lista_semanas or opcao is True:
                print(lista_semanas[rece])
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

            else:
                print("Apenas pesquisas por semanas.")
                break


except Exception:
    print(" Aconteceu algo...")


