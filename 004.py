#Ahora nos adentramos en un territorio más técnico: realizar una búsqueda lineal en una lista de n datos sin repetición y ordenada de menor a mayor. Debemos medir el tiempo que tarda la búsqueda en diferentes tamaños de datos.

import time

def busqueda_lineal(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

# Código para medir tiempos
def medir_busqueda_lineal(n):
    lista = list(range(n))
    valor = lista[int(0.7 * len(lista))]
    tiempos = []
    for _ in range(10):
        inicio = time.time()
        busqueda_lineal(lista, valor)
        fin = time.time()
        tiempos.append(fin - inicio)
    return sum(tiempos) / len(tiempos)


#Complejidad: La búsqueda lineal tiene una complejidad de O(n), ya que en el peor de los casos recorremos toda la lista.