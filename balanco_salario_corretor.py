import os
fixo = 1500.00
comissao_fixa = 200.00
nome = str(input("Coloque aqui o nome do corretor: "))
numero_de_vendas = int(input(f"Olá {nome}, quantas vendas você realizou? "))
vendas = 0
comissao_por_venda = 0
while vendas < numero_de_vendas:
     valor_venda = float(input("Qual foi o valor da venda desse imovel? "))    
     comissao_por_venda = (5/100) * valor_venda    
     vendas += 1    
     comissao_por_venda += 1    
     os.system("cls")
comissao_por_cada_venda = comissao_fixa * numero_de_vendas
salario = fixo + comissao_por_cada_venda + comissao_por_venda
print(f"Óla {nome}, seu salario esse mês é de {salario}")