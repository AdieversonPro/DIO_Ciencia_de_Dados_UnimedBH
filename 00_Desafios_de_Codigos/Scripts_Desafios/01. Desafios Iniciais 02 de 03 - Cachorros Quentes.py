# Desafio 02 - Cachorros Quentes

valores = input().split() 

cachorros_quentes = int(valores[0])
participantes = int(valores[1])

while cachorros_quentes >= 1 and participantes <=1000:
  print(f'{cachorros_quentes/participantes:.2f}')
  break