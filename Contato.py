AGENDA = {}
AGENDA['caio'] = {'telefone':'15998137846','email':'teste@gmail.com'}

print("\n[OPEN].........................CONTATOS\n\n")

def MostrarContato():
    for contato in AGENDA:
        if AGENDA:
            print("NOME:",contato)
            print("TELEFONE:", AGENDA[contato]['telefone'])
            print("EMAIL:", AGENDA[contato]['email'])
            print("------------->")

def AdicionarContato(contato,telefone,email):
    AGENDA[contato] = {'telefone':telefone,'email':email}

def Menu():
    print("\n_______________________________________")
    print("1-MOSTRAR CONTATO")
    print("2-ADICIONAR NOVO CONTATO")
    print("3-EDITAR CONTATO")
    print("4-EXCLUIR CONTATO")
    print("5-FECHAR CONTATO")
    print("_______________________________________")

def ExcluirContato(contato):
    AGENDA.pop(contato)
    print("----->Excluiu {}".format(contato))

while True:
    Menu()
    opcao = input("\nEscolha uma opçâo: ")

    if opcao == '1':
        MostrarContato()
    elif opcao == '2' or opcao == '3':
        contato = input("------>Nome do contato: ")
        telefone = input("------>Telefone contato: ")
        email = input("------>E-mail contato: ")
        AdicionarContato(contato, telefone, email)
    elif opcao == '4':
        contato = input("------>EXCLUIR: ")
        ExcluirContato(contato)
    elif opcao == '5':
        print(".......................................")
        break
    else:
        print("Palavras não existem no dicionario.")
