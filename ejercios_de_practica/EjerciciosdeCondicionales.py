# Ejercicio 1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

# age = int(input('Dime tu edad: '))
# if age >= 18:
#     print('¡Eres mayor de Edad!')
# else:
#     print('¡Eres menor de Edad!')


# Ejercicio 2
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

# password = 'contraseña'
# confirmacion = input('Contraseña: ')

# if password == confirmacion.lower():
#     print('\nAcceso permitido!')
# else:
#     print('Acceso denegado\n\n¡Claves no coinciden!')


#Ejercicio 3
#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

# print('Ingresa 2 numeros para saber su division entre si')
# numerador = int(input('Numerador: '))
# denominador = int(input('Denominador: '))

# if denominador != 0:
#     print(f'La division es {round(numerador / denominador, 2)}')
# else:
#     print('¡No puedes dividir entre cero!')


#Ejercicio 4
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

# numero = int(input('Ingresa un numero: '))

# if numero % 2 == 0:
#     print(f'¡El numero {numero} es par!')
# else:
#     print(f'¡El numero {numero} es inpar!')


#Ejercicio 5
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

# edad = int(input('¿Cual es tu edad?: '))
# ingreso = float(input('Ingresos mensuales: '))

# if edad > 16 and ingreso >= 1000:
#     print('Te toca tributar')
# else:
#     print('No te toca tributar')


#Ejercicio 6
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

# name = input('Cual es tu nombre: ')
# sex = input('Sexo (f o m): ')

# if name[:1].lower() < 'm' and sex[:1].lower() == 'f' or name[:1].lower() > 'n' and sex[:1].lower() == 'm':
#     print('Estas en el grupo A')
# else:
#     print('Estas en el grupo B')


#Ejercicio 7
#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 20000€ y 35000€	20%
# Entre 35000€ y 60000€	30%
# Más de 60000€	45%

# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

# renta_anual = float(input('¿Cual es tu renta anual?: '))

# if renta_anual < 10000:
#     print(f'Su impositivo es del 5% y debe pagar {round(renta_anual * 5 / 100, 2)}')
# elif renta_anual < 20000:
#     print(f'Su impositivo es del 15% y debe pagar {round(renta_anual * 15 / 100, 2)}')
# elif renta_anual < 35000:
#     print(f'Su impositivo es del 20% y debe pagar {round(renta_anual * 20 / 100, 2)}')
# elif renta_anual < 60000:
#     print(f'Su impositivo es del 30% y debe pagar {round(renta_anual * 30 / 100, 2)}')
# else:
#     print(f'Su impositivo es del 45% y debe pagar {round(renta_anual * 45 / 100, 2)}')


# Ejercicio 8
# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más

# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.