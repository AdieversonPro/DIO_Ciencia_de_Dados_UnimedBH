# Desafio 02 - Papagaio Poliglota

while True:
    try:
        posicao_perna = input().split()
        if posicao_perna[0] == "esquerda":
            print("ingles")
        if posicao_perna[1] == "direita":
            print("frances")
        if posicao_perna[2] == "nenhuma":
            print("portugues")
        if posicao_perna[3] == "ambas":
            print("caiu")
    except EOFError:
        break