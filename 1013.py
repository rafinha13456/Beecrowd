lista = list(input().split(" "))

lista = [int(i) for i in lista]

maior01 = (lista[0]+lista[1]+abs(lista[0]-lista[1]))/2

maiorX3 = (maior01+lista[2]+abs(maior01-lista[2]))/2

print(f'{int(maiorX3)} eh o maior')