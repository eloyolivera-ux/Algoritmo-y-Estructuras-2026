from list_ import List
from Queue import Queue
from super_heroes_data import superheroes


class Personaje:

    def __init__(self, name, alias, real_name, bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.bio = bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        return f"{self.name} - {self.real_name} - {self.first_appearance}"


def by_name(personaje):
    return personaje.name


def by_real_name(personaje):
    if personaje.real_name is None:
        return ""
    return personaje.real_name


def by_first_appearance(personaje):
    return personaje.first_appearance


lista_heroes = List()

lista_heroes.add_criterion("name", by_name)
lista_heroes.add_criterion("real_name", by_real_name)
lista_heroes.add_criterion("first_appearance", by_first_appearance)

for hero in superheroes:

    lista_heroes.append(
        Personaje(
            hero["name"],
            hero["alias"],
            hero["real_name"],
            hero["short_bio"],
            hero["first_appearance"],
            hero["is_villain"]
        )
    )


print()
print("Lista Ordenada")
print()

lista_heroes.sort_by_criterion("name")

for hero in lista_heroes:
    print(hero)

print()
print("buscar The Thing y Rocket Raccoon ")
print()

posicion = lista_heroes.search("The Thing", "name")

if posicion is not None:
    print("The Thing:", posicion + 1)

posicion = lista_heroes.search("Rocket Raccoon", "name")

if posicion is not None:
    print("Rocket Raccoon:", posicion + 1)


print()
print("Listar todos los villanos")
print()

for hero in lista_heroes:

    if hero.is_villain:
        print(hero)

print()
print("Cola de villanos")
print()

cola_villanos = Queue()

for hero in lista_heroes:

    if hero.is_villain:
        cola_villanos.arrive(hero)


while cola_villanos.size() > 0:

    hero = cola_villanos.attention()

    if hero.first_appearance < 1980:
        print(hero)

print()
print("Listar super que empiezan con Bl, G, My y W")
print()

lista_Superheroes = List()

for hero in lista_heroes:

    if not hero.is_villain:
        lista_Superheroes.append(hero)

print()
print("Superhéroes que comienzan con Bl:")
lista_Superheroes.filter_start_with("Bl")
print()

print("Superhéroes que comienzan con G:")
lista_Superheroes.filter_start_with("G")
print()

print("Superhéroes que comienzan con My:")
lista_Superheroes.filter_start_with("My")
print()

print("Superhéroes que comienzan con W:")
lista_Superheroes.filter_start_with("W")
print()


print("lista ordenado por nombre real")
print()

lista_heroes.sort_by_criterion("real_name")

for hero in lista_heroes:
    print(hero)


print()
print("lista ordenado por fecha de aparicion")
print()

lista_Superheroes.add_criterion("first_appearance", by_first_appearance)
lista_Superheroes.sort_by_criterion("first_appearance")

for hero in lista_Superheroes:
    print(hero)

print()
print("Modificar el nombre de Ant Man")
print()

posicion = lista_heroes.search("Ant Man", "name")

if posicion is not None:

    hero = lista_heroes[posicion]

    hero.real_name = "Scott Lang"

    print(hero)

print()
print("mostrar personajes segun su biografia")
print()

lista_heroes.filter_contain_on_bio(
    ["time-traveling", "suit"]
)


print()
print("Eliminacion de electro y zemo")
print()

electro = lista_heroes.delete_value("Electro", "name")

if electro is not None:
    print()
    print("Electro estaba en la lista:")
    print(electro)
    print()

baron_zemo = lista_heroes.delete_value("Baron Zemo", "name")

if baron_zemo is not None:
    print()
    print("Baron Zemo estaba en la lista:")
    print(baron_zemo)
    print()