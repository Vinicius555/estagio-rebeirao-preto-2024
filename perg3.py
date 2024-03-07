# 3) Descubra a lógica e complete o próximo elemento:


# a) 1, 3, 5, 7, ___
# Apenas números ímpares ou incrementando de 2 em 2
def letra_a():
    sequencia = [1, 3, 5, 7]
    prox_elemento = sequencia[-1] + 2
    return prox_elemento  # 9


# b) 2, 4, 8, 16, 32, 64, ____
# O próximo número é o dobro do anterior
def letra_b():
    sequencia = [2, 4, 8, 16, 32, 64]
    prox_elemento = sequencia[-1] * 2
    return prox_elemento  # 128


# c) 0, 1, 4, 9, 16, 25, 36, ____
# O próximo número é o indíce elevado a 2
def letra_c():
    sequencia = [0, 1, 4, 9, 16, 25, 36]
    prox_elemento = len(sequencia) ** 2
    return prox_elemento  # 49


# d) 4, 16, 36, 64, ____
# O próximo número é o quadrado perfeito dos números pares
def letra_d():
    sequencia = [4, 16, 36, 64]
    prox_elemento = (len(sequencia) * 2 + 2) ** 2
    return prox_elemento  # 100


# e) 1, 1, 2, 3, 5, 8, ____
# Sequencia de fibonacci
def letra_e():
    sequencia = [1, 1, 2, 3, 5, 8]
    prox_elemento = sequencia[-1] + sequencia[-2]
    return prox_elemento  # 13


# f) 2,10, 12, 16, 17, 18, 19, ____
# O próximo número sera 200 pois é um sequência de números que começam com a letra D
def letra_f():
    sequencia = [2, 10, 12, 16, 17, 18, 19]
    sequencia.append(200)
    return sequencia[-1]  # 200
