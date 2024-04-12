from random import choice
import string

print("\n[X]Gerador de SENHA\n")

while True:
    tamanho_da_senha = int(input("-->Tamanho da senha: "))
    contem = string.digits + string.ascii_letters 
    senha = ('')

    for w in range(tamanho_da_senha):
        senha += choice(contem)
    print("\nGerador aleatorio: ",senha)

    
