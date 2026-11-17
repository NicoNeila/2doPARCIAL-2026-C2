from ejercicio_01 import Pokemon


class PokemonNoEncontrado(Exception):
    pass


class Pokedex:

    def __init__(self):
        self._pokemones = []

    def agregar(self, pokemon):
        # si ya hay uno con ese id lo reemplaza en el mismo lugar
        for i in range(len(self._pokemones)):
            if self._pokemones[i].id == pokemon.id:
                self._pokemones[i] = pokemon
                return
        self._pokemones.append(pokemon)

    def obtener(self, id):
        for pokemon in self._pokemones:
            if pokemon.id == id:
                return pokemon
        raise PokemonNoEncontrado(f"No existe el Pokémon con id {id}.")

    def listar(self):
        return list(self._pokemones)   # devuelvo una copia

    def cantidad(self):
        return len(self._pokemones)


def pokedex_del_examen():
    # datos del examen, la uso para probar los ejercicios
    pokedex = Pokedex()
    pokedex.agregar(Pokemon(1, "Bulbasaur", "Planta", "Veneno", 45, 49, 49, 45, 1))
    pokedex.agregar(Pokemon(2, "Ivysaur", "Planta", "Veneno", 60, 62, 63, 60, 1))
    pokedex.agregar(Pokemon(3, "Venusaur", "Planta", "Veneno", 80, 82, 83, 80, 1))
    pokedex.agregar(Pokemon(4, "Charmander", "Fuego", "", 39, 52, 43, 65, 1))
    pokedex.agregar(Pokemon(5, "Charmeleon", "Fuego", "", 58, 64, 58, 80, 1))
    pokedex.agregar(Pokemon(6, "Charizard", "Fuego", "Volador", 78, 84, 78, 100, 1))
    pokedex.agregar(Pokemon(25, "Pikachu", "Electrico", "", 35, 55, 40, 90, 1))
    pokedex.agregar(Pokemon(26, "Raichu", "Electrico", "", 60, 90, 55, 110, 1))
    pokedex.agregar(Pokemon(133, "Eevee", "Normal", "", 55, 55, 50, 55, 1))
    pokedex.agregar(Pokemon(134, "Vaporeon", "Agua", "", 130, 65, 60, 65, 1))
    pokedex.agregar(Pokemon(135, "Jolteon", "Electrico", "", 65, 65, 60, 130, 1))
    pokedex.agregar(Pokemon(136, "Flareon", "Fuego", "", 65, 130, 60, 65, 1))
    return pokedex


# TEORIA
# Que no tiene que andar revisando si le volvió None: si el id no existe salta el error en el momento y lo puede manejar con un try/except.


if __name__ == "__main__":
    pokedex = pokedex_del_examen()
    print(pokedex.cantidad())
    print(pokedex.obtener(25))
    try:
        pokedex.obtener(999)
    except PokemonNoEncontrado as error:
        print("Error:", error)