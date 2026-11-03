from pokemon_data import pokemons
from tree import BinaryTree
from queue_ import Queue

class Pokemon():

    def __init__(self, nombre, numero, tipos, debilidades, mega, gigamax):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos
        self.debilidades = debilidades
        self.mega = mega
        self.gigamax = gigamax

    def __str__(self):
        return (f"#{self.numero} {self.nombre} | tipos: {', '.join(self.tipos)} | "
                f"debil a: {', '.join(self.debilidades)} | "
                f"mega: {self.mega} | gigamax: {self.gigamax}")

def proximity_search(root, text, result):
    if root is not None:
        proximity_search(root.left, text, result)
        if text in root.value.lower():
            result.append(root.other_values)
        proximity_search(root.right, text, result)

tree_name = BinaryTree()
tree_number = BinaryTree()
tree_type = BinaryTree()

for data in pokemons:
    pokemon = Pokemon(data['nombre'], data['numero'], data['tipos'],
                      data['debilidades'], data['mega'], data['gigamax'])

    tree_name.insert_node(pokemon.nombre, pokemon)
    tree_number.insert_node(pokemon.numero, pokemon)

    for t in pokemon.tipos:
        node = tree_type.search(t)
        if node is None:
            tree_type.insert_node(t, [pokemon]) 
        else:
            node.other_values.append(pokemon)     

try:
    number = int(input('Ingrese el número del Pokémon: '))
    node = tree_number.search(number)
    if node is not None:
        print(node.other_values)
    else:
        print('No se encontró ese número')
except ValueError:
    print('Tenés que ingresar un número entero')

text = input('Ingrese el nombre o parte del nombre: ').lower().strip()
result = []
proximity_search(tree_name.root, text, result)

if len(result) > 0:
    for pokemon in result:
        print(pokemon)
else:
    print('No se encontró ningún Pokémon')

input('Presioná Enter para continuar...')

tipos_a_mostrar = ['fantasma', 'fuego', 'acero', 'electrico']

for tipo in tipos_a_mostrar:
    print(f'\nPokémon de tipo {tipo}:')
    node = tree_type.search(tipo)
    if node is not None:
        for pokemon in node.other_values:
            print(pokemon.nombre)
    else:
        print('No hay Pokémon de ese tipo')

input('Presioná Enter para continuar...')

def inorden_pokemon(root):
    if root is not None:
        inorden_pokemon(root.left)
        print(f'#{root.other_values.numero} {root.other_values.nombre}')
        inorden_pokemon(root.right)

print('\nListado ascendente por número:')
inorden_pokemon(tree_number.root)

input('Presioná Enter para continuar...')

print('\nListado ascendente por nombre:')
inorden_pokemon(tree_name.root)

input('Presioná Enter para continuar...')

print('\nListado por nivel por nombre:')
tree_name.by_level()

input('Presioná Enter para continuar...')

def debiles_frente_a(root, tipos, result):
    if root is not None:
        debiles_frente_a(root.left, tipos, result)
        pokemon = root.other_values
        if any(t in pokemon.debilidades for t in tipos):
            result.append(pokemon.nombre)
        debiles_frente_a(root.right, tipos, result)

for nombre in ['Jolteon', 'Lycanroc', 'Tyrantrum']:
    node = tree_name.search(nombre)
    if node is None:
        print(f'\n{nombre} no está cargado')
        continue

    tipos = node.other_values.tipos
    print(f'\nDébiles frente a {nombre} (tipos: {", ".join(tipos)}):')

    result = []
    debiles_frente_a(tree_name.root, tipos, result)
    for nombre_pokemon in result:
        print(nombre_pokemon)
    input('\nPresioná Enter para continuar...')

def mostrar_tipos(root):
    if root is not None:
        mostrar_tipos(root.left)
        print(f'{root.value}: {len(root.other_values)}')
        mostrar_tipos(root.right)

print('\nCantidad de Pokémon por tipo:')
mostrar_tipos(tree_type.root)
input('\nPresioná Enter para continuar...')

cant_mega = 0
cant_gigamax = 0

pendientes = Queue()
pendientes.arrive(tree_name.root)

while pendientes.size() > 0:
    node = pendientes.attention()
    pokemon = node.other_values

    if pokemon.mega:
        cant_mega += 1
    if pokemon.gigamax:
        cant_gigamax += 1

    if node.left is not None:
        pendientes.arrive(node.left)
    if node.right is not None:
        pendientes.arrive(node.right)

print(f'\nPokémon con megaevolución: {cant_mega}')
print(f'Pokémon con forma gigamax: {cant_gigamax}')




