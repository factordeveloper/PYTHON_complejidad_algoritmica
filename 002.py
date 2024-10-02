#Ahora vamos a jugar un poco. Nuestro objetivo es crear una función que reciba dos listas: una con los números que el usuario da y otra con los números que piensa la máquina, luego determine cuántas "picas" y "fijas" hay (como en el juego de picas y fijas).


def picas_y_fijas(usuario, maquina):
    picas = 0
    fijas = 0
    for i in range(len(usuario)):
        if usuario[i] == maquina[i]:
            fijas += 1
        elif usuario[i] in maquina:
            picas += 1
    return picas, fijas

#Complejidad: Este algoritmo tiene una complejidad de O(n), porque debe recorrer ambas listas de tamaño n una vez.