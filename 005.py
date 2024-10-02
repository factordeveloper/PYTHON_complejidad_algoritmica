#Ahora vamos a mejorar nuestra búsqueda utilizando un enfoque más eficiente: la búsqueda binaria.

def busqueda_binaria(lista, valor):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Código para medir tiempos
def medir_busqueda_binaria(n):
    lista = list(range(n))
    valor = lista[int(0.7 * len(lista))]
    tiempos = []
    for _ in range(10):
        inicio = time.time()
        busqueda_binaria(lista, valor)
        fin = time.time()
        tiempos.append(fin - inicio)
    return sum(tiempos) / len(tiempos)


#Complejidad: La búsqueda binaria tiene una complejidad de O(log n), lo que la hace significativamente más rápida para listas grandes.