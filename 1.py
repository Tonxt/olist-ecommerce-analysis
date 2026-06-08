'''lista = [64, 25, 12, 45]

def burbujeo(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


lista = [64, 25, 12, 45]

'''
'''def insertar(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i+1,len(lista)):
                if lista[minimo] > lista[j]:
                    minimo = j
        aux = lista[i]
        lista[i] = lista[minimo]
        lista[minimo] = aux
    return lista
'''
def fibonacci(n):
    lista = []
    a,b = 0,1
    for i in range(n):
        lista.append(a)
        a,b = b,a+b
    return lista


print(fibonacci(10))






