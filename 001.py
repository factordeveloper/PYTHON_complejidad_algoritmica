#1. Imprimir una lista de datos aleatorios

import random

def imprimir_lista(n):
    lista = [random.randint(0, (n // 2) ** 2) for _ in range(n)]
    for elemento in lista:
        print(elemento)

#Complejidad: La complejidad de esta función es O(n), ya que tanto generar la lista como imprimir cada uno de los elementos requiere un tiempo proporcional al tamaño de la lista.