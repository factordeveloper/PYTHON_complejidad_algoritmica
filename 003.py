#La siguiente tarea es sencilla: imprimimos solo el primer elemento de una lista de datos aleatorios.

def imprimir_primer_elemento(n):
    lista = [random.randint(0, (n // 2) ** 2) for _ in range(n)]
    print(lista[0])

#Complejidad: Aunque generar la lista tiene complejidad O(n), la operación de acceso es O(1). Por lo tanto, en este caso la complejidad es O(n) por la generación de la lista.