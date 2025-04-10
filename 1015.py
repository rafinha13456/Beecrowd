from math import sqrt

p1 = list(input().split(" "))
p2 = list(input().split(" "))

p1 = [float(i) for i in p1]
p2 = [float(i) for i in p2]

distancia = sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)

print("%.4f" % distancia)
