def usar_la_fuerza(mochila: list[str], indice: int = 0, contador: int = 0):
    
    if indice >= len(mochila):
        return False, contador
    if mochila[indice] == "sable de luz":
        return True, contador + 1
    else 
        return usar_la_fuerza(mochila, indice + 1, contador + 1)



mochila_jedi = ["comida", "ropa", "linterna", "mapa", "sable de luz"]

encontrado, cantidad = usar_la_fuerza(mochila_jedi)

if encontrado:
    print("El Jedi encontró el sable de luz")
else:
    print("No se encontró el sable de luz")

print("Objetos revisados:", cantidad)