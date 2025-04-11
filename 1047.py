h1, m1, h2, m2 = map(int, input().split())

inicio = h1 * 60 + m1
fim = h2 * 60 + m2

if inicio == fim:
    duracao = 24 * 60
elif inicio < fim:
    duracao = fim - inicio
else:
    duracao = (24 * 60 - inicio) + fim

horas = duracao // 60
minutos = duracao % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
