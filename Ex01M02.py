numeros = [1,2,3,4,5,6,7,8,9,10]
pares = []
impares = []
c = 0
for c in range(len(numeros)):
    if numeros[c] % 2 == 0:
        pares.append(numeros[c])
        print(pares)
    else:
        impares.append(numeros[c])
        print(impares)
