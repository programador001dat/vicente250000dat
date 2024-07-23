loja = ("\n__>Eletronicos Vendas-Celulares   \n")
print(loja,"\n Av. General Carneiro/Sorocaba                                      N°1579")
telefone = ("(15)991145-8728")
comerciante = (" Caio Vicente Ramos")
print(" Telefone:",telefone,"                Comerciante:",comerciante)
precoM = " 2299,90$ "
precoR = " 3000,00$ "
precoS = " 1499,99$ "
class Eletronicos:
    def __init__(self):
        self.Motorola = "Motorola Moto G54"
        self.Apple = "iPhone 14 "
        self.Samsung = "Samsung Galaxy"

chamar_loja = Eletronicos()
print("\n")
print("__________________________________________________________________________")
print(" PREÇO:",precoM, chamar_loja.Motorola,"Realme C53 Dual Sim 256 Gb 8 Gb Ram ")
print(" PREÇO:",precoR, chamar_loja.Apple,"Apple iPhone 14 128GB Estelar")
print(" PREÇO:",precoS, chamar_loja.Samsung,"Samsung Galaxy S21 128GB 5G Ram")
print("__________________________________________________________________________")
def Motorola():
    Motorola = " Motorola G54"
    if Motorola:
        print(" Voce selecionou para comprar ->",Motorola)       
def Iphone():
    Iphone = " Iphone 14"
    if Iphone:
        print(" Voce selecionou para comprar ->",Iphone)        
def Samsung():
    Samsung = " Samsung Galaxy S21"
    if Samsung:
        print(" Voce selecionou para comprar ->",Samsung)
def Escolher():
    print("_[1]_MOTOROLA G54",)
    print("_[2]_IPHONE 14")
    print("_[3]_SAMSUNG S21")   
Escolher()
def Cadastro():
    cadastro = ([''])
    if cadastro:
        nome = input("__>Informe proprietario Cartão: ")
        email = input("__>Informe seu E-mail: ")
        dados = input("__>Numero do Cartão: ")
        cvv = input("__>CVV: ")
        data = input("__>Data Vencimento: ")
    
    with open('nome.txt','w')as cadastro:
        cadastro = cadastro.write(nome)
        
    with open('email.txt','w')as cadastro:
        cadastro = cadastro.write(email)
    
    with open('dados.txt','w')as cadastro:
        cadastro = cadastro.write(dados)
        
    with open('cvv.txt','w')as cadastro:
        cadastro = cadastro.write(cvv)
        
    with open('data.txt','w')as cadastro:
        cadastro = cadastro.write(data)
        print("Registro escrito com sucesso!")
while True:
    opcao = input(" Selecao: ")
    if opcao == '1':
        Motorola()
        Cadastro()
        Escolher()
        print('Comprado tá na mão kk')
        print("\n")
    if opcao == '2':
        Iphone()
        Cadastro()
        Escolher
        print('comprado tá na mão kk')
        
        print("\n")
    if opcao == '3':
        Samsung()
        Cadastro()
        Escolher()
        print('comprado tá na mão kk')
        print("\n")
    if opcao == '':
        print('Produto nao encontrado')
        break
    elif():
        print('Produto nao encontrado')
        Escolher()
        
       


