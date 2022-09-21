# while True:
    # print('Se ejecuto el print')
    
# while False:
#     print('No salimos más de acá!')

# ejecución_nro = 0
# while True:
#     ejecución_nro += 1
#     print ('Se ejecutó el print nro:', ejecución_nro)

# Ejemplo1

# repetir_menu = True
# while repetir_menu:
#     print('''
# ==============
#         Menu
# ==============
# 1. Retirar efectivo.
# 2. Cambiar Contraseña.
# 3. Salir
# ''')
#     opción_elegida = input('Ingrese la operación a realizar: ')
#     if opción_elegida == '1':
#         print('Retiro efectivo.')
#     elif opción_elegida == '2':
#         print('Cambio la contraseña.')
#     elif opción_elegida == '3':
#         print('Hasta luego')
#         repetir_menu = False
#     else:
#         print('Vuelva a intentar con una opción válida.')
        
# Ejemplo2

# hasta = int(input('Ingrese un númeor hasta donde quiere sumar'))
# suma = 0
# while hasta:
#     suma += hasta
#     hasta -= 1
    
# print(f'la suma es {suma}')

# Break

# edad_perro = 0
# while True:
#     print('Guau!')
#     if edad_perro <= 15:
#         edad_perro += 1
#     else:
#         break

# Continue

# numero = 0
# while numero < 10:
#     numero += 1
#     if numero%2 == 0:
#         continue
#     print (numero)
           
# print('Salí del while')

# Usos del Pass

# if True:
#     pass

# nombre = input('Dime tu nombre: ')
# if nombre == '****':
#     pass

# While - Else

# condicion = 10
# while condicion:
#     valor1 = 10
#     suma = valor1 + condicion
#     if suma == 20:
#         break
#     print(f'La suma dio de resultado {suma}')
#     condicion -= 1  
# else:
#     print('Pasé por el else')
    
# variable = 'Acá ya estamos fuera del bucle'
# print (variable)

# For

# indice = 0
# lista = [10,9,8,7,6,5,4,3,2,1]
# for dato_de_la_lista in lista:
#     valor1 = 10
#     suma = valor1 + dato_de_la_lista
#     print(f'La suma dio de resultado {suma}')
    
# variable = 'Acá ya estamos fuera del bucle'
# print(variable)
# print(lista)

# Enumerate

# lista = [10,9,8,7,6,5,4,3,2,1]
# for indice, valor_de_la_lista in enumerate(lista):
#     valor1 = 10
#     suma = valor1 + valor_de_la_lista
#     print(f'La suma dio de resultado {suma}')
#     lista[indice] = valor_de_la_lista * 2
    
# variable = 'Acá ya estamos fuera del bucle'
# print(variable)
# print(lista)

# Range

# for numero in range (5,9,2):
#     valor1 = 10
#     suma = valor1 + numero
#     print(f'La suma dio de resultado {suma}')

# for numero in range(5, 9):
#     # if numero == 7:
#     #     break
#     if numero == 7:
#         continue
#     print(numero)
# else:
    # print('Pasé por el else')
