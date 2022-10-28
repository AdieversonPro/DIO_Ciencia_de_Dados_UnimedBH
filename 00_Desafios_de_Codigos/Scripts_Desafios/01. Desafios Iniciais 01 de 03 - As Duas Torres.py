# Desafio 01 - As Duas Torres 

entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])
soma_dia = float(diametro1 + diametro2)
while distancia < 10000 and diametro2 < 100 and soma_dia < distancia:
    print (f'{distancia/soma_dia:.2f}')
    break
