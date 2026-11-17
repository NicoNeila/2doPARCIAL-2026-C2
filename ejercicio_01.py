class Pokemon:
    """Pokémon de la Pokédex."""

    def __init__(self, id, nombre, tipo1, tipo2, hp, ataque, defensa, velocidad, generacion):
        self._id = id          # el id no se puede cambiar después
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2     # si no tiene segundo tipo es ""
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.generacion = generacion

    @property
    def id(self):
        return self._id

    def __str__(self):
        if self.tipo2 == "":
            return f"#{self.id} {self.nombre} ({self.tipo1})"
        return f"#{self.id} {self.nombre} ({self.tipo1}/{self.tipo2})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, otro):
        if not isinstance(otro, Pokemon):
            return False
        return self.id == otro.id

    def __hash__(self):
        # si defino __eq__ también tengo que definir __hash__, uso el id
        return hash(self.id)


# TEORIA
# La identidad es el id; nombre, tipos, estadísticas y generación son estado.
# No: la identidad no debería cambiar después de construido el objeto, por eso id es de solo lectura.


if __name__ == "__main__":
    bulbasaur = Pokemon(1, "Bulbasaur", "Planta", "Veneno",