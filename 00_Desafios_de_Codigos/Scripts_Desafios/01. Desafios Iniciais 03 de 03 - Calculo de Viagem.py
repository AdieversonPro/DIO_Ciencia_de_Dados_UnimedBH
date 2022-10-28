# Desafio 03 - Calculo de Viagem

valores = input().split()

tempo = int(valores[0])
velocidade = int(valores[1])
distancia = float(velocidade*tempo)
print(f'{distancia/12:.3f}')