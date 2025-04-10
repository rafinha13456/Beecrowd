nome = input()
salario_fixo = float(input())
total_vendas = float(input())

comissao = total_vendas * 0.15 + salario_fixo

#print("TOTAL = R$ %.2f", % comissao)
print(f'TOTAL = R$ {comissao:.2f}')