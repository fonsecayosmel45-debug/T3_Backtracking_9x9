ENERGIA_INICIAL = 18

laberinto_vista = [
    [1,   1,   1,   1,  99,  1,  1,  1, "I"],
    [1,  99,  99,   1,  99,  1, 99,  1, 99],
    [1,   1,  99,   1,   1,  1, 99,  1, 99],
    [99,  1,  99,   1,  99, 99, 99,  1, 99],
    [1,   1,  99,  -1,   1,  1,  1,  3, 99],
    [-2, 99,  99,   1,  99, 99, 99,  1,  1],
    [1,  99,   1,  -1,   1,  1,  1,  1, 99],
    [1,  99,  99,  99,  99,  2, 99,  1, 99],
    ["F", 1,   3,   1,   1,  1, 99,  1,  1],
]

laberinto = [
    [1,  1,  1,  1, 99, 1, 1, 1, 0],   
    [1, 99, 99, 1, 99, 1, 99, 1, 99],
    [1,  1, 99, 1,  1, 1, 99, 1, 99],
    [99, 1, 99, 1, 99, 99, 99, 1, 99],
    [1,  1, 99, -1, 1, 1, 1, 3, 99],
    [-2,99, 99, 1, 99, 99, 99, 1,  1],
    [1, 99, 1, -1, 1, 1, 1, 1, 99],
    [1, 99,99, 99,99, 2, 99, 1, 99],
    [0,  1,  3,  1, 1, 1, 99, 1,  1],  
]

FILAS = len(laberinto)
COLS  = len(laberinto[0])

INICIO = (0, 8)   
FIN    = (8, 0)  

def imprimir_matriz(m):
    for fila in m:
        print(" ".join(f"{c:>3}" for c in fila))
    print()


def resolver_laberinto():
    visitados = set()
    camino = []

    exito, camino_encontrado, energia_final = backtrack(
        INICIO[0],
        INICIO[1],
        ENERGIA_INICIAL,
        camino,
        visitados
    )

    print("Laberinto original (con I y F):")
    imprimir_matriz(laberinto_vista)

    if exito:
        print("Se encontró un camino válido hasta la salida.")
        print(f"Energía restante al llegar: {energia_final}")
        print("Matriz de camino (I, F, * ruta, 99 muro, . libre):")
        matriz_camino = construir_matriz_camino(camino_encontrado)
        imprimir_matriz(matriz_camino)
    else:
        print("NO se encontró ningún camino con la energía disponible.")
        print("Se muestran solo muros (99) y libres (.)")
        matriz_camino = construir_matriz_camino([])
        imprimir_matriz(matriz_camino)


def backtrack(fila, col, energia, camino, visitados):
    camino.append((fila, col))
    visitados.add((fila, col))

    if (fila, col) == FIN:
        return True, list(camino), energia


    movimientos = [(0, -1), (1, 0), (-1, 0), (0, 1)]

    for df, dc in movimientos:
        nf, nc = fila + df, col + dc

        if not (0 <= nf < FILAS and 0 <= nc < COLS):
            continue

        if (nf, nc) in visitados:
            continue

        valor = laberinto[nf][nc]

        if valor == 99:
            continue 

        nueva_energia = energia - valor 

        if nueva_energia < 0:
            continue

        exito, camino_ok, energia_final = backtrack(
            nf, nc, nueva_energia, camino, visitados
        )
        if exito:
            return True, camino_ok, energia_final

    camino.pop()
    visitados.remove((fila, col))
    return False, [], energia


def construir_matriz_camino(camino):
    camino_set = set(camino)
    matriz = []

    for f in range(FILAS):
        fila = []
        for c in range(COLS):
            if (f, c) == INICIO:
                fila.append(" I")
            elif (f, c) == FIN:
                fila.append(" F")
            elif laberinto[f][c] == 99:
                fila.append("99")
            elif (f, c) in camino_set:
                fila.append(" *")
            else:
                fila.append(" .")
        matriz.append(fila)
    return matriz


if __name__ == "__main__":
    resolver_laberinto()
