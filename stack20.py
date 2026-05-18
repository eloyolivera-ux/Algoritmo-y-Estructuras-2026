from typing import Any


# Clase Stack
class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Any:
        return self.__elements.pop()

    def size(self) -> int:
        return len(self.__elements)
   
    def on_top(self) -> Any:
        if self.size() > 0:
            return self.__elements[-1]

def contrario(direccion):

    if direccion == "norte":
        return "sur"

    elif direccion == "sur":
        return "norte"

    elif direccion == "este":
        return "oeste"

    elif direccion == "oeste":
        return "este"

    elif direccion == "noreste":
        return "suroeste"

    elif direccion == "noroeste":
        return "sureste"

    elif direccion == "sureste":
        return "noroeste"

    elif direccion == "suroeste":
        return "noreste"


movimientos = Stack()

n = input("Cantidad de movimientos: ")
n = int(n)

print("Recorrido de ida:")

for i in range(n):

    pasos = input("Pasos: ")
    pasos = int(pasos)

    direccion = input("Direccion: ")

    movimientos.push((pasos, direccion))

    print("Caminar", pasos, "pasos hacia", direccion)


print("Regreso del robot:")

while movimientos.size() > 0:

    pasos, direccion = movimientos.pop()

    print("Caminar", pasos, "pasos hacia", contrario(direccion))