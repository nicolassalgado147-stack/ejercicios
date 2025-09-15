#separar los numeros pares e impares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []

for i in range(len(numeros)):
    if numeros [i] % 2 == 0:
        pares.append([numeros[i]])
    else:
        impares.append(numeros[i])

        print ("pares:", pares)
        print ("impares:", impares)
