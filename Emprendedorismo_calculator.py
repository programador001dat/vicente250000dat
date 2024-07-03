import calendar
ano = 2024
dia = 7
print(calendar.month(ano,dia))
print("(+)Exemplo: nao começou a semana na DOMINGO, digite 00 para pular, e avancar para proxima pergunta. ")
print("   Esse programa faz calculos com numero Inteiros/Flutuantes, Exemplo: 50+50+ 44.15+50.12+ [?].[?]+[?].\n\n")
while True:
    
    try:
    
        print("_>Primeira semana.")
        w = float(input(" Domingo, Ganho do dia [COMECOU]?: "))
        a = float(input(" Segunda-Feira, Ganho do dia[01]?: "))
        b = float(input(" Terça-Feira, Ganho do dia[02]?: "))
        c = float(input(" Quarta-Feira, Ganho do dia[03]?: "))
        d = float(input(" Quinta-Feira, Ganho do dia[04]?: "))
        e = float(input(" Sexta-Feira, Ganho do dia[05]?: "))
        f = float(input(" Sabado, Ganho do dia[06]?: "))
        soma_primeira_semana = (a+b+c+d+e+f+w)
        print("\n_>Segunda semana.")

        aa = float(input(" Domingo, Ganho do dia?[09]?: "))
        ab = float(input(" Segunda-Feira, Ganho do dia[10]?: "))
        ac = float(input(" Terça-Feira, Ganho do dia[11]?: "))
        ad = float(input(" Quarta-feira, Ganho do dia[12]?: "))
        ae = float(input(" Quinta-feira, Ganho do dia[13]?: "))
        af = float(input(" Sexta-Feira, Ganho do dia[14]?: "))
        aw = float(input(" Sabado, Ganho do dia[15]?: "))
        soma_segunda_semana = (aa+ab+ac+ad+ae+af)
        print("\n_>Terceira semana.")

        ba = float(input(" Domingo, Ganho do dia[16]?:"))
        bb = float(input(" Segunda_Feira, Ganho do dia[17]?: "))
        bc = float(input(" Terça-Feira, Ganho do dia?[18]: "))
        bd = float(input(" Quarta-Feira, Ganho do dia[19]?: "))
        be = float(input(" Quinta-Feira, Ganho do dia[20]?: "))
        bf = float(input(" Sexta-Feira, Ganho do dia[21]?: "))
        bw = float(input(" Sabado, Ganho do dia[22]?: "))
        soma_terceira_semana = (ba+bb+bc+bd+be+bf+bw)
        print("\n_>Quarta semana.")
        
        ca = float(input(" Domingo, Ganho do dia[23]?:"))
        cb = float(input(" Segunda-Feira, Ganho do dia[24]?: "))
        cc = float(input(" Terça-Feira, Ganho do dia[25]?: "))
        cd = float(input(" Quarta-Feira, Ganho do dia[26]?: "))
        ce = float(input(" Quinta-Feira, Ganho do dia[27]?: "))
        cf = float(input(" Sexta-Feira, Ganho do dia[28]?: "))
        cw = float(input(" Sabado, Ganho do dia[29]?:"))
        soma_quarta_semana = (ca+cb+cc+cd+ce+cf+cw)
        print("\n_>Ultima semana.")

        da = float(input(" Domingo, Ganho do dia[30]?: "))
        db = float(input(" Segunda-Feira, Ganho do dia[31]?: "))
        dc = float(input(" Terça-Feira, Ganho do dia?: "))
        dd = float(input(" Quarta-Feira, Ganho do dia?: "))
        de = float(input(" Quinta-Feira, Ganho do dia?: "))
        df = float(input(" Sexta-Feira, Ganho do dia?: "))
        dw = float(input(" Sabado, Ganho do dia?: "))
        print("\n")
               
        soma_semana_final = (da+db+dc+dd+de+df+dw)
        final = (soma_primeira_semana+soma_segunda_semana+soma_terceira_semana+soma_quarta_semana+soma_semana_final)
        print("$",final,"REAL do Mês.")
        print("\n_________________________________")


    except:
        print("\n ->Se voce teclar Enter sem nenhum resultado. Traceback: ValueError error in String.\n\n")
