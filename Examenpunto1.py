from super_heroes_data import superheroes

def buscar_capitan_america(lista, indice=0):
    if indice == len(lista):
        return None
    if lista[indice]["name"] == "Captain America":
        return True
    return  buscar_capitan_america(lista, indice + 1)

def lista_personajes(lista, indice=0):
    if indice == len(lista):
        return None
    
    print(lista[indice]["name"])
    lista_personajes(lista,indice + 1 )

if buscar_capitan_america(superheroes):
    print("Capitan America esta en la lista")
else:
    print("Capitan America no esta en la lista")

lista_personajes(superheroes)
