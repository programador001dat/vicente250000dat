#Script passa ou não passa de ano. 
print("\n__>SISTEMA ESCOLA\n")

escola = ("E.E.PLINÍO RODRIGUES DE MORAES")
print(escola)
print("_________________________________________________")
aluno = ("Caio Vicente Ramos ")
serie = ("           ANO: 3C")
print("ALUNO:", aluno, serie,"\n_________________________________________________" )
print("\nNOTAS ADMINISTRATIVAS DO ALUNO\n")

matematica = ("Matematica")
portugues = ("Portugues")
ciencias = ("Ciencias")
filosofia = ("Filosofia")
artes = ("Artes")
geografia = ("Geografia")
passo = 5
reprovo = 5

#PARA MUDAR A NOTA, BASTA; ALTERAR: ONE_ = 'nota_aqui' TWO_ = 'nota_aqui' THREE__ = 'nota_aqui' FOUR_ = 'nota_aqui' exemplos.
#ESSAS NOTAS SAO ARMAZENADAS EM VARIAVEIS.
#POR ULTIMO CALCULE A NOTA NA VARIAVEL FINAL: materia:_final(nota+nota+nota+nota)/4

one_matematica = "6"
two_matematica = "5"
three_matematica = "3"
four_matematica = "3"

matematica_final = (6+5+3+3)/4

if matematica_final >= passo:
    print("MATERIA:",matematica,"   NOTA: ", matematica_final,"    APROVADO")
elif matematica_final <= reprovo:
    print("MATERIA:",matematica,"   NOTA: ", matematica_final,"    REPROVADO")

one_portugues = "5"
two_portugues = "6"
three_portugues = "5"
four_portugues = "9"

portugues_final = (5+6+5+9)/4

if portugues_final >= passo:
    print("MATERIA:",portugues,"    NOTA: ", portugues_final,"    APROVADO")
elif portugues_final <= reprovo:
    print("MATERIA:",portugues,"    NOTA: ", portugues_final, "   REPROVADO")

one_ciencias = "8"
two_ciencias = "7"
three_ciencias = "6"
four_ciencias = "5"

ciencias_final = (8+7+6+5)/4

if ciencias_final >= passo:
    print("MATERIA:",ciencias,"     NOTA: ", ciencias_final,"     APROVADO")
elif ciencias_final <= reprovo:
    print("MATERIA:",ciencias,"     NOTA: ", ciencias_final,"     REPROVADO")

one_filosofia = "5"
two_filosofia = "5"
three_filosofia = "7"
four_filosofia = "7"

filosofia_final = (5+5+7+7)/4

if filosofia_final >= passo:
    print("MATERIA:",filosofia,"    NOTA: ", filosofia_final,"     APROVADO")
elif filosofia_final <= reprovo:
    print("MATERIA:",filosofia,"    NOTA: ", filosofia_final,"     REPROVADO")

one_artes = "7"
two_artes = "5"
three_artes = "5"
four_artes = "1"

artes_final = (7+5+5+1)/4

if artes_final >= passo:
    print("MATERIA:",artes,"        NOTA: ", artes_final,"     APROVADO")
elif artes_final <= reprovo:
    print("MATERIA:",artes,"        NOTA: ", artes_final,"     REPROVADO")

one_geografia = "4"
two_geografia = "8"
three_geografia = "4"
four_geografia = "5"

geografia_final = (4+8+4+5)/4

if geografia_final >= passo:
    print("MATERIA:",geografia,"    NOTA: ", geografia_final,"    APROVADO")
elif geografia_final <= reprovo:
    print("MATERIA:",geografia,"    NOTA: ", geografia_final,"    REPROVADO")

    
