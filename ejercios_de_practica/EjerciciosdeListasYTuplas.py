#Ejercicio 1
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

# asignature = ['Matematica', 'Fisica', 'Quimica', 'Historia', 'Lengua']
# print(asignature)


#Ejercicio 2
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

# asignature = ['Matematica', 'Fisica', 'Quimica', 'Historia', 'Lengua']
# print('Yo estudio:')
# for i in asignature:
#     print(i, '')


#Ejercicio 3
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

# asignatures = ['Matematica', 'Fisica', 'Quimica', 'Historia', 'Lengua']
# nota = []
# for asignature in asignatures:
#     score = input(f'Nota obtenida en {asignature}: ')
#     nota.append(score)
# for i in range(len(asignatures)):
#     print(f'La nota obtenida en {asignatures[i]}: {nota[i]}')


#Ejercicio 4
#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

# iteration = int(input('¿Cuantos numeros tiene la loteria primitiva?: '))
# numbers = []
# for i in range(iteration):
#     data = int(input('Escribe los numeros ganadores, uno por uno: '))
#     numbers.append(data)
#     numbers.sort()
# print(f'Los numeros ganadores son: {numbers}')


#Ejercicio 5
#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

# elements = [1,2,3,4,5,6,7,8,9,10]
# for i in range(1,11):
#     print(elements[-i], end=', ')


#Ejercicio 6
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

# asignatures = ['Matematica', 'Fisica', 'Quimica', 'Historia', 'Lengua']
# user = []
# for i in asignatures:
#     note = int(input(f'Nota obtenida en {i}: '))
#     if note < 5:
#         user.append(i)
    
# print(f'Reprobaste {user}')


#Ejercicio 7
#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

# abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# for i in range(len(abc),0,-1):
#     if i % 3 == 0:
#         del abc[i-1]
# print(abc)


#Ejercicio 8
#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

# palintromo = input('Escribe una palabra para ver si es palindromo: ')
# if palintromo.lower().replace(' ','') == palintromo[::-1].lower().replace(' ',''):
#     print('Es palindromo!')
# else:
#     print('No es palindromo!')


#Ejercicio 9
#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

# word = input('Escribe una palabra: ')
# vocals = ('a','e','i','o','u')
# for i in vocals:
#     contador = 0
#     for j in word:
#         if i == j:
#             contador += 1
#     print(f'La letra {i} apacece {contador} veces en la palabra')


#Ejercicio 10
#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

# price = (50, 75, 46, 22, 80, 65, 8)
# print(price)
# print(f'{min(price)} es el precio menor')
# print(f'{max(price)} es el precio mayor')


#Ejercicio 11
#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.