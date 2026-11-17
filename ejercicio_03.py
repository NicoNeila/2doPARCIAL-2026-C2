from ejercicio_02 import PokemonNoEncontrado, pokedex_del_examen

ARISTAS_DEL_EXAMEN = [(1, 2), (2, 3), (4, 5), (5, 6), (25, 26), (133, 134), (133, 135), (133, 136)]


def descendientes(origen_id, pokedex, aristas):
    pokedex.obtener(origen_id)  # si no existe, obtener lanza PokemonNoEncontrado

    destinos = []
    for origen, destino in aristas:
        if origen == origen_id:
            destinos.append(destino)

    if destinos == []:            # caso base: no evoluciona en nada
        return []

    resultado = []
    for destino in destinos:
        resultado.append(destino)
        # caso recursivo: primero bajo por este destino y después sigo con el siguiente
        resultado.extend(descendientes(destino, pokedex, aristas))
    return resultado


# TEORIA
# descendientes(4): tiene destino 5, lo agrega y llama a descendientes(5)
# descendientes(5): tiene destino 6, lo agrega y llama a descendientes(6)
# descendientes(6): no tiene destinos, es el caso base y devuelve []
# Al volver, descendientes(5) da [6] y descendientes(4) da [5, 6].


if __name__ == "__main__":
    pokedex = pokedex_del_examen()
    print(descendientes(1, pokedex, ARISTAS_DEL_EXAMEN))
    print(descendientes(133, pokedex, ARISTAS_DEL_EXAMEN))
    print(descendientes(6, pokedex, ARISTAS_DEL_EXAMEN))
    try:
        descendientes(999, pokedex, ARISTAS_DEL_EXAMEN)
    except PokemonNoEncontrado as error:
        print("Error:", error)