from super_heroes_data import superheroes
from Queue_ import Queue

def ordenar_nombre(personaje):
    return personaje["name"]

def ordenar_nombre_real(personaje):
    return personaje["real_name"] or ""

def ordenar_fecha(personaje):
    return personaje["first_appearance"]

print("")
print("listado ordenado")
superheroes.sort(key=ordenar_nombre)
for personaje in superheroes:
    print(personaje["name"])

print("")
print("buscar The Thing y Rocket Raccoon ")

for i, personaje in enumerate(superheroes):
    if personaje["name"] == "The Thing":
        print("The Thing esta en la posicion:", i)
    
    if personaje["name"] == "Rocket Raccoon":
        print("Rocket Raccoon esta en la posicion:", i)

print("")
print("Listar todos los villanos")
for personaje in superheroes:
    if personaje["is_villain"]:
        print(personaje["name"])

print("")
print("Cola de villanos")

cola = Queue()

for personaje in superheroes:
    if personaje["is_villain"]:
        cola.arrive(personaje)

while cola.size() > 0:
    personaje = cola.attention()
    if personaje["first_appearance"] < 1980:
        print(personaje["name"], personaje["first_appearance"])

print("")
print("listar super que enmpiezan con Bl, G, My y W")

for personaje in superheroes:
    if not personaje["is_villain"]:
        nombre = personaje["name"]

        if nombre.startswith("Bl") or nombre.startswith("G") or nombre.startswith("My") or nombre.startswith("W"):
            print(nombre)

print("")
print("lista ordenado por nombre real")

superheroes.sort(key=ordenar_nombre_real)
for personaje in superheroes:
    print(personaje["real_name"])

print("")
print("\060[1mlista ordenado por fecha de aparicion\033[0m")

superheroes.sort(key=ordenar_fecha)

for personaje in superheroes:
    print(personaje["name"], personaje["first_appearance"])

print("")
print("modificar el nombre de ant man ")

for personaje in superheroes:
    if personaje["name"] == "Ant Man":
        personaje["real_name"] = "Scott Lang"
        print(personaje)
        break

print("")
print("mostrar personajes segun su biografia")

for personaje in superheroes:
    bio = personaje["short_bio"].lower()
    if "time-traveling" in bio or "suit" in bio:
        print(personaje["name"])