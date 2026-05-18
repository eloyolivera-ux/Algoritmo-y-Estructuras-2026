class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, value):
        self.__elements.append(value)

    def pop(self):
        return self.__elements.pop()

    def size(self):
        return len(self.__elements)
   
    def on_top(self) -> Any:
        if self.size() > 0:
            return self.__elements[-1]


personajes = Stack()

n = int(input("Cantidad de personajes: "))

for i in range(n):

    nombre = input("Nombre: ")
    peliculas = int(input("Peliculas: "))

    personajes.push((nombre, peliculas))


aux = Stack()

pos = 1
pos_rocket = 0
pos_groot = 0

print("Mas de 5 peliculas:")
print("Empiezan con C, D o G:")

while personajes.size() > 0:

    nombre, peliculas = personajes.pop()

    aux.push((nombre, peliculas))

    if nombre == "Rocket Raccoon":
        pos_rocket = pos

    if nombre == "Groot":
        pos_groot = pos

    pos += 1

    if peliculas > 5:
        print(nombre, peliculas)

    if nombre == "Black Widow":
        print("Black Widow:", peliculas)

    if nombre[0] == "C" or nombre[0] == "D" or nombre[0] == "G":
        print(nombre)

while aux.size() > 0:
    personajes.push(aux.pop())

print("Posicion Rocket:", pos_rocket)
print("Posicion Groot:", pos_groot)