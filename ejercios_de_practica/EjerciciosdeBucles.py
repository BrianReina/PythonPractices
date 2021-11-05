#Ejercicio 1
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

# word = input('Write a word: ')
# for i in range(10):
#     print(word)


#Ejercicio 2
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

# age = int(input('What is your age: '))
# for i in range(1, age+1):
#     print(i)


#Ejercicio 3
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

# number = int(input('Write a number: '))
# for i in range(1, number+1):
#     if i % 3 == 0:
#         print(i, end=', ')


#Ejercicio 4
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

# number = int(input('Write a number: '))
# for i in range(number, -1, -1):
#     print(i, end=', ')


#Ejercicio 5
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# capital = float(input('Capital a invertir: '))
# interes = float(input('Interes anual: '))
# year = int(input('Por cuantos años: '))
# for i in range(year):
#     capital *= (1+interes)
#     print(f'inversion obtenida en el año {i+1} es: {round(capital, 2)}')


#Ejercicio 6
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
# *
# **
# ***
# ****
# *****

# user = int(input('Escribe un numero para definir la altura del triangulo: '))
# for i in range(user):
#     print('*'*(i+1))


#Ejercicio 7
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

# for i in range(1, 11):
#     for j in range(1,11):
#         print(i*j, end='\t')
#     print('')


#Ejercicio 8
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

# user = int(input('Escribe un numero para dibujar un triangulo rectangulo: '))
# for i in range(1, user+1, 2):
#     for j in range(i, 0, -2):
#         print(j, end=' ')
#     print('')


#Ejercicio 9
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

# password = 'contraseña'
# user = input('What is the password?: ')
# while password != user.lower():
#     print('Ingrese la contraseña correcta')
#     user = input('What is the password?: ')
# print('Acceso autorizado!')


#Ejercicio 10
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.