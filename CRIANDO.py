imprimir = ['Sol_Celestial.PNG','PaisagemRiacho.JPG','NavioNalfragado.PNG','Lua_Eclipse.JPG','Floresta.PNG','TubaraoMartelo.WEB','BMW-foguete.PNG']
lista_final = []                    #lista recebera valores da lista acima.

while imprimir:
    lista = imprimir.pop()          #lista armazena oque foi removido com metedo .POP(), armazenamos em outra variavel lista.
    print(f"\tImprimindo roteiro: ->{lista}")
    lista_final.append(lista)       #adicionamos oque foi armazenado na lista e adicionamos a lista_final.
    print(f"{lista} ->adicionado a lista de concluido.\n")



