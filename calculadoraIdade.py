from datetime import date as dt

hoje=dt.today()

nasc_ano=int(input("Digite o ano que você nasceu: "))
nasc_mes=int(input("Digite o mes que você nasceu: "))
nasc_dia=int(input("Digite o dia do seu aniversário: "))

hoje_ano=hoje.year
hoje_mes=hoje.month
hoje_dia=hoje.day

anos=float(hoje_ano - nasc_ano)
meses=float(hoje_mes - nasc_mes)
dias=float(hoje_dia - nasc_dia)

vida=(anos*365.25) + (meses*30.4375) + (dias*1)
dias_vida=round(vida)

idade_float=float(dias_vida/365.25)
idade_int=int(idade_float)
dif_idade=float(idade_float-idade_int)
meses_float=float(dif_idade*12)
meses_int=int(meses_float)
dif_mes=float(meses_float-meses_int)
dias_float=float(dif_mes*30.4375)
dias_int=int(dias_float)


print("Você tem {} anos, {} meses e {} dias de idade.".format(idade_int, meses_int, dias_int))




