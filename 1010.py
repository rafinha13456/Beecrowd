linha1 = list(input().split(" "))
linha2 = list(input().split(" "))

valor1 = float(linha1[1])*float(linha1[2])

valor2 = float(linha2[1])*float(linha2[2])

valor_fin = valor1+valor2

print("VALOR A PAGAR: R$ %.2f" % valor_fin)