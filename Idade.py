dia_nasc = int(input('Dia que nasceu: '))
mes_nasc = int(input('Mês que nasceu: '))
ano_nasc = int(input('Ano que nasceu: '))

ano_atual = 2021
mes_atual = 1
idade = ano_atual - ano_nasc
if mes_atual < mes_nasc:
 print('Sua idade é: ' , idade - 1)