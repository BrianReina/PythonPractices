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