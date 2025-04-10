pi = 3.14159

lista = list(input().split(" "))

lista = [float(i) for i in lista]

tri = lista[0]*lista[2]/2
cir = pi*lista[2]**2
tra =(lista[0]+lista[1])*lista[2]/2
qua = lista[1]**2
ret = lista[0]*lista[1]

print(f"TRIANGULO: {tri:.3f}\nCIRCULO: {cir:.3f}\nTRAPEZIO: {tra:.3f}\nQUADRADO: {qua:.3f}\nRETANGULO: {ret:.3f}")