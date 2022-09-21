#Set

# lista = ['soy', 'una', 'lista', 2, True]
# tupla = ('soy', 'una', 'tupla', 2, True)
# conjunto = {'soy', 'una', 'conjunto', 1, True}

# # lista_vacia = []
# # tupla_vacia = ()
# # conjunto_vacio = {}
# # conjunto_vacio2 = set()
# # print(type(lista_vacia))
# # print(type(tupla_vacia))
# # print(type(conjunto_vacio))
# # print(type(conjunto_vacio2))

# lista[1] = 'uno'
# print(lista)
#La lista reemplaza el str porque tiene un índice. El conjunto no tiene índice ni tampoco duplica los valores
#El conjunto es inmutable. Puede contener tuplas pero no listas.

# lista_prueba = [1, 2, 3, 'hola', 'como', 'estas', ('otra', 'lista')]
# tupla_prueba = (1, 2, 3, 'hola', 'como', 'estas', ('otra', 'lista'))
# conjunto_prueba = set(tupla_prueba)
# conjunto_prueba2 = set(range(10))
# print(conjunto_prueba2)

#Iterable = Elemento que se puede ir recorriendo de valor a valor

# auto = {'v8', 'Negro', (6, 'blindadas')}
# # print(auto)

#Add

# auto.add('descapotable')
# print(auto)

#Update

# auto = {'v8', 'Negro', (6, 'blindadas')}
# lista = ['soy', 'una', 'lista']
# tupla = ('soy', 'una', 'tupla')
# cadena = 'soy una cadena'
# rango = range(15)
# auto.update(lista)
# print(auto)

# auto = {'v8', 'Negro', (6, 'blindadas')}
# print(len(auto))

#Discard y Remove.

# auto = {'v8', 'Negro', (6, 'blindadas')}
# # auto.discard('lista') #Si no está lo que se quiere eliminar, no pasa nada.
# auto.remove('lista') #Si no está lo que se quiere eliminar, error.
# print(auto)

# auto = {'v8', 'Negro', (6, 'blindadas')}
# print('descapotable' in auto)
# print('caño de escape' not in auto)

#Clear

# auto = {'v8', 'Negro', (6, 'blindadas')}
# auto.clear()
# auto = set()
# print(auto)

#Pop

# auto = {'v8', 'Negro', (6, 'blindadas')}
# print(auto)
# valor = auto.pop()
# print(auto)
# print(valor)

#Diccionarios

# dicc = {
#     0: ['soy', 'una', 'lista'], 
#     'string': ('soy', 'una', 'tupla')
#     ('tupla', 'llave'): 'la tupla es mi llave'
# }

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4
# }
# print(auto)

#Acceso, mutabilidad, asignación, agregado de valores

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4
# }
# # print(auto['motor']) #Si no existe la clave, genera error.
# print(auto.get('motor')) #Si no existe la clave, no genera error. Genera None.
# print(auto.get('caño de escape', 45))
# print(auto.get('caño de escape', input('Que valor querés: ')))

# print(auto)
# auto['motor'] = 'v12'
# print(auto['motor'])
# print(auto)

#Update

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4
# }

# pepe = (1, 2)
# auto.update({pepe: 'valor1', 'llave1': 'valor2', 'motor': 'v12'})
# print(auto)

#In

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4
# }
# print('motor' in auto)
# print( 'v8' in auto)

#Del

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4
# }

# del auto['color']
# print(auto)

#Clear

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4
# }
# auto.clear()
# # auto = {}
# print(auto)

#Pop

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4
# }

# # print(auto)
# # valor = auto.pop('motor')
# # print(auto)
# # print(valor)

# print(auto)
# valor = auto.pop('ricardo', 'All Boys')
# print(auto)
# print(valor)

# animales = {'elefante': ''}

# animales_a_agregar = {'perro': 'Bobby', 'tigre': 'Pepe', 'mono': 'Homero'}
# animales.update(animales_a_agregar)

# animales['elefante'] = 'Trompis'
# animales['delfin'] = 'Manolo'

# print(animales)