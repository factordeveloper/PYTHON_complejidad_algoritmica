# Complejidad del algoritmo de Insertion Sort

def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

#Complejidad: La complejidad promedio es O(n^2) debido a los dos bucles anidados. Sin embargo, si la lista está casi ordenada, su complejidad se acerca a O(n).