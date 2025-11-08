#sem compreensao de listas
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

#com compreensao de listas
numeros_2 = [1, 2, 3, 4, 5]
numeros_dobrados_2 = [numero_2 *  2 for numero_2 in numeros_2]

print(numeros_dobrados_2)

#melhorando
numeros_3 = [1, 2, 3, 4, 5]

def dobro(numero_3):
    return numero_3 * 2

numeros_dobrados_3 = [dobro(numero_3) for numero_3 in numeros_3]

print(numeros_dobrados_3)