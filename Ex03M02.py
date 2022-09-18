lista1 = [1,4,3]
lista2 = [3,5,1]
resultadotreu = []
def soma(lista1, lista2):
    for i in range(len(lista1)):
        resultado = lista1[i] + lista2[i]
        print(f"Indices da lista1:{lista1[i]} lista 2:{lista2[i]}")
        resultadotreu.append(resultado)
    print(resultadotreu)

soma(lista1, lista2)