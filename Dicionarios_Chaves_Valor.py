#Lista de SQL python, contador de chave valor.
import sys
import os
def Biblioteca():
    sql = {}

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>  Lista de Contatos.py caio  >>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    sql['caio'] = {'Endereco':'SaoPaulo-SP','Telefone':'1599892832','Profissao':'Programador Python',}                            #adicionamos um valor no dicionario.
    sql['nayane'] = {'Endereco':'Bahia-BH','Telefone':'1599892832','Profissao':'Programadora Css e Javascript',}           #adicionamos um valor no dicionario.
    sql['monica'] = {'Endereco':'Goiania-GO','Telefone':'1599892832','Profissao':'Programadora HTML',}                       #adicionamos um valor no dicionario.
    sql['joao'] = {'Endereco':'Itu-SP','Telefone':'1599892832','Profissao':'Programador C+ JavaScript',}                            #adicionamos um valor no dicionario.
    sql['jessica'] = {'Endereco':'Recife-RE','Telefone':'1599892832','Profissao':'Programadora Perl e BashScripting,'}    #adicionamos um valor no dicionario.

    for a in list[sql]:                                         #correndo a lista de senhas com ({a}).
#        print(a)                                                 #verbose lista sql
        print(len(sql))                                        #Contador de valores da lista sql.
        print(">>tamanho da lista acima.")
        break

    try:


        while True:
            
            nome = (str(input(">>pesquisar usuario:\t\t")))
            rece = str(nome)                                                           #string recebe string

            if rece in sql or nome is True:                                      #Verifico metodo String, stringNome fez or Comparacao, verifico True e True.
                print(f"(!)achamos algo sobre: {rece}")                   
                print(sql[rece])
                print("\n\n")
                
            else:
                print(f" {rece} nao encontrado!")
                break

    except Exception:
        print("Até logo.")


Biblioteca()

