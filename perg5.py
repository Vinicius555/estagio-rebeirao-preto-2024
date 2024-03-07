"""
5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

"""


def inverter(string):
    saida = ""
    for i in range(len(string) - 1, - 1, - 1):
        saida += string[i]
    return saida


texto_normal = "Olá, mundo!"
texto_invetido = inverter(texto_normal)
print("String Normal:", texto_normal)
print("String invertida:", texto_invetido)
