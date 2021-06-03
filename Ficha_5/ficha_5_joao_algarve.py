"""
Trabalho realizado por:
        João Algarve
        PDM-B
        1º ano
        nº 45304
"""
#--------------------------------1--------------------------------

lista=[1,5,3,6,22,45,63,30,344,22,12,25,10]

print(lista[::-1])

for i in range(0, len(lista)):
    for j in range(i+1, len(lista)):
        if(lista[i] == lista[j]):
            print("O numero mais repetido é", lista[j], "e o seu indice é", i-1);

#--------------------------------1--------------------------------

#--------------------------------2--------------------------------

tuplo = ()

adicionar = None

resposta = True

while (resposta):

    adicionar = input("\nInsira um numero ('terminar' para terminar): ")

    if (adicionar == "terminar"):
        resposta = False

    else:
        tuplo += (int(adicionar),)

print(tuplo)

tuplo_par = ()

for i in range (len(tuplo)):
    if (tuplo[i] % 2 == 0) :
        tuplo_par += (tuplo[i],)

print("Algarismos pares: ", tuplo_par,"\n")

#--------------------------------2--------------------------------

#--------------------------------3--------------------------------

numeros=(10,15,3,6,99,45,63,30,344,22,4,25,10)

print("A lista tem {0} valores de comprimento".format(len(numeros)))

print("Número maximo:",max(numeros), "\nNúmero minimo:",min(numeros))

numeros2 = (21, 53, 23, 54, 22, 2, 1, 13)

numeros3 = numeros + numeros2
print("\nnumeros3:",numeros3)

numeros3_inpar=()

for i in range ( len(numeros3) ):
    if ( numeros3[i] % 2 != 0) :
        numeros3_inpar += (numeros3[i],)

print("\nNúmeros impares:", numeros3_inpar, "\n")

numeros3_mul5 = ()

for i in range ( len(numeros3) ):
    if ( numeros3[i] % 5 == 0) :
        numeros3_mul5 += (numeros3[i],)

print("Números multiplos de 5:", numeros3_mul5,"\n")
#--------------------------------3--------------------------------

#--------------------------------4--------------------------------

import numpy as np

def max_val(tabela_4x3):
    return np.max(tabela_4x3)

tabela_4x3 =[]

for i in range(12):
    val = float(input("Insira {0}º numero: ".format(i+1)))
    tabela_4x3.append(val)

np.array(tabela_4x3)

tabela_4x3 = np.reshape(tabela_4x3, (4,3))

print("{0}\nO numero mais elevado da tabela 4x3 é: {1}".format(tabela_4x3, max_val(tabela_4x3)))
#--------------------------------4--------------------------------