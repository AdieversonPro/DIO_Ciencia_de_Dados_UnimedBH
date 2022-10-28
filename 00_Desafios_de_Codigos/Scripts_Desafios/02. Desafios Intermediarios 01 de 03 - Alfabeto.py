# Desafio 01 - Alfabeto

letra = input().upper()
  
def positions(letra):
    for i in letra:
        print((ord(i) & 27), end =" ")

positions(letra)