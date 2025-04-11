def decompor_valor(valor):
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    valor_centavos = int(round(valor * 100))
    print("NOTAS:")
    for nota in notas:
        nota_centavos = int(nota * 100)
        qtd = valor_centavos // nota_centavos
        valor_centavos %= nota_centavos
        print(f"{qtd} nota(s) de R$ {nota:.2f}")
    print("MOEDAS:")
    for moeda in moedas:
        moeda_centavos = int(round(moeda * 100))
        qtd = valor_centavos // moeda_centavos
        valor_centavos %= moeda_centavos
        print(f"{qtd} moeda(s) de R$ {moeda:.2f}")
entrada = float(input())
decompor_valor(entrada)