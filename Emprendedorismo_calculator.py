import calendar
import os
os.system("clear")
ano = 2024
mes = 7
print("\n",calendar.month(ano,mes))
print("(!)Exemplo: nao começou a semana na DOMINGO, digite Zero.0 para pular, e avancar para proxima linha. ")
print("  °Esse programa faz calculos com numero Inteiros/Flutuantes, Exemplo: 50+50+ 44.15+50.12+ [?].[?]+[?].")
print("  °Pagamento Ifood são depositados toda Quarta-feira. Ctrl+Z Sair do Script.\n\n")
while True:
    
    try:
    
        print(" [1]Primeira semana...")
        w = float(input(" Domingo.          [COMECOU]$?: "))
        a = float(input(" Segunda-feira.      dia[01]$?: "))
        b = float(input(" Terca-feira.        dia[02]$?: "))
        c = float(input(" Quarta-feira.       dia[03]$?: "))
        d = float(input(" Quinta-feira.       dia[04]$?: "))
        e = float(input(" Sexta-feira.        dia[05]$?: "))
        f = float(input(" Sabado.             dia[06]$?: "))
        soma_primeira_semana = (a+b+c+d+e+f+w)
        
        print("\n [2]Segunda semana...")
        aa = float(input(" Domingo.            dia[07]$?: "))
        ab = float(input(" Segunda-feira.      dia[08]$?: "))
        ac = float(input(" Terca-feira.        dia[09]$?: "))
        ad = float(input(" Quarta-feira.       dia[10]$?: "))
        ae = float(input(" Quinta-feira.       dia[11]$?: "))
        af = float(input(" Sexta-feira.        dia[12]$?: "))
        aw = float(input(" Sabado.             dia[13]$?: "))
        soma_segunda_semana = (aa+ab+ac+ad+ae+af+aw)
        
        print("\n [3]Terceira semana...")
        ba = float(input(" Domingo.            dia[14]$?: "))
        bb = float(input(" Segunda-feira.      dia[15]$?: "))
        bc = float(input(" Terca-feira.        dia[16]$?: "))
        bd = float(input(" Quarta-feira.       dia[17]$?: "))
        be = float(input(" Quinta-feira.       dia[18]$?: "))
        bf = float(input(" Sexta-feira.        dia[19]$?: "))
        bw = float(input(" Sabado-Feira.       dia[20]$?: "))
        soma_terceira_semana = (ba+bb+bc+bd+be+bf+bw)
        
        print("\n [4]Quarta semana...")
        ca = float(input(" Domingo.            dia[21]$?: "))
        cb = float(input(" Segunda-feira.      dia[22]$?: "))
        cc = float(input(" Terca-feira.        dia[23]$?: "))
        cd = float(input(" Quarta-feira.       dia[24]$?: "))
        ce = float(input(" Quinta-feira.       dia[25]$?: "))
        cf = float(input(" Sexta-feira.        dia[26]$?: "))
        cw = float(input(" Sabado.             dia[27]$?: "))
        soma_quarta_semana = (ca+cb+cc+cd+ce+cf+cw)
        
        print("\n [5]Ultima semana...")
        da = float(input(" Domingo.            dia[28]$?: "))
        db = float(input(" Segunda-feira.      dia[29]$?: "))
        dc = float(input(" Terca-feira.        dia[30]$?: "))
        dd = float(input(" Quarta-feira.       dia[31]$?: "))
        de = float(input(" Quinta-feira.   dia[FECHOU]$?: "))
        df = float(input(" Sexta-feira.    dia[FECHOU]$?: "))
        dw = float(input(" Sabado.         dia[FECHOU]$?: "))
        print("_________________________________")       
        soma_semana_final = (da+db+dc+dd+de+df+dw)
        final = float(soma_primeira_semana+soma_segunda_semana+soma_terceira_semana+soma_quarta_semana+soma_semana_final)
        print("$",final,"REAL final do Mês.")
        print("_________________________________\n\n")


    except:
        print("\n ->Se voce teclar Enter sem nenhum resultado. Traceback: ValueError error in String.\n\n")
