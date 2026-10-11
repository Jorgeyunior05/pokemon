from clases.pokemon import Pokemon

# Variable global: lista compartida de Pokémon del simulador.
pokemones = []


def buscar_pokemon(nombre):
    """Busca un Pokémon por nombre y devuelve el objeto o None."""
    for pokemon in pokemones:
        if pokemon.nombre.lower() == nombre.lower():
            return pokemon
    return None


def capturar_pokemon():
    print("\n--- Capturar Pokémon ---")
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("El nombre no puede quedar vacío.")
        return

    if buscar_pokemon(nombre):
        print("Ya existe un Pokémon con ese nombre.")
        return

    tipo = input("Tipo: ").strip()
    if not tipo:
        print("El tipo no puede quedar vacío.")
        return

    # Variables locales con valores iniciales por defecto.
    pokemon = Pokemon(nombre, tipo)
    pokemones.append(pokemon)
    print(f"¡{nombre} fue agregado al equipo!")


def seleccionar_pokemon(mensaje="Escribe el nombre del Pokémon: "):
    nombre = input(mensaje).strip()
    pokemon = buscar_pokemon(nombre)
    if pokemon is None:
        print("No se encontró ese Pokémon.")
    return pokemon


def entrenar_pokemon():
    pokemon = seleccionar_pokemon("¿Qué Pokémon quieres entrenar? ")
    if pokemon is None:
        return

    print("1. Mejorar todas las estadísticas")
    print("2. Mejorar una estadística")
    print("3. Mejorar dos estadísticas")
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        pokemon.entrenar()
    elif opcion == "2":
        estadistica = input("¿Cuál? (ataque, defensa, salud): ").strip().lower()
        pokemon.entrenar(estadistica)
    elif opcion == "3":
        primera = input("Primera (ataque, defensa, salud): ").strip().lower()
        segunda = input("Segunda (ataque, defensa, salud): ").strip().lower()
        pokemon.entrenar(primera, segunda)
    else:
        print("Opción no válida.")


def mostrar_pokemones():
    if not pokemones:
        print("Todavía no has capturado ningún Pokémon.")
        return

    for pokemon in pokemones:
        pokemon.mostrar_info()
        print(f"Poder total: {pokemon.calcular_poder()}")


def combatir():
    if len(pokemones) < 2:
        print("Necesitas al menos dos Pokémon para combatir.")
        return

    print("Pokémon disponibles:")
    for pokemon in pokemones:
        print(f"- {pokemon.nombre} (salud: {pokemon.salud})")

    atacante = seleccionar_pokemon("¿Quién va a atacar? ")
    if atacante is None:
        return

    objetivo = seleccionar_pokemon("¿A quién va a atacar? ")
    if objetivo is None:
        return

    if atacante is objetivo:
        print("Un Pokémon no puede atacarse a sí mismo.")
        return

    atacante.atacar(objetivo)


def liberar_pokemon():
    pokemon = seleccionar_pokemon("¿Qué Pokémon quieres liberar? ")
    if pokemon is None:
        return

    nombre = pokemon.nombre
    pokemones.remove(pokemon)
    # Se actualiza el contador de la clase al retirar el Pokémon del equipo.
    Pokemon.cantidad_pokemon = max(0, Pokemon.cantidad_pokemon - 1)
    print(f"{nombre} fue retirado del equipo.")


def menu():
    while True:
        print("\n========== SIMULADOR POKÉMON ==========")
        print("1. Capturar Pokémon")
        print("2. Entrenar Pokémon")
        print("3. Ver información de todos")
        print("4. Combatir")
        print("5. Calcular total de Pokémon")
        print("6. Liberar Pokémon")
        print("0. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            capturar_pokemon()
        elif opcion == "2":
            entrenar_pokemon()
        elif opcion == "3":
            mostrar_pokemones()
        elif opcion == "4":
            combatir()
        elif opcion == "5":
            Pokemon.total_pokemons()
        elif opcion == "6":
            liberar_pokemon()
        elif opcion == "0":
            print("¡Gracias por usar el simulador Pokémon!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
