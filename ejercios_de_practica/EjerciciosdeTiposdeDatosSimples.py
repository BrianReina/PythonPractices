#Ejercicio 1
#Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

#print('Hola Mundo')


#Ejercicio 2
#Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

#variable = 'Hola Mundo!'
#print(variable)


#Ejercicio 3
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

#user = input('Cual es tu nombre?: ')
#print(f'Hola {user}')


#Ejercicio 4
#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética (3+2/2-5)**2.

#operacion = ((3+2)/(2*5))**2
#print(f'El resultado de la operacion es: {operacion}')


#Ejercicio 5
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

#worked_hours = int(input('¿Cuantas horas trabajas en la semana? :'))
#cost_x_hours = int(input('Costo por horas?: '))
#salary = worked_hours * cost_x_hours
#print(f'Your salary of the week is: {salary}')

#Ejercicio 6 
#Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos puede ser calculada de la siguiente forma:

#entero = int(input('¿Introduce un numero entero: '))
#suma = (entero*(entero+1))/2
#print(f'La suma desde 1 hasta {entero} es {suma}')


#Ejercicio 7
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

#peso_usuario = float(input('¿Cual es tu peso? en Kg: '))
#estatura_usuario = float(input('¿Cual es tu estatura? en m: '))
#imc = peso_usuario / (estatura_usuario**2)
#imc = round(imc, 2)
#print(f'Tu indice de masa corporal es {imc}')


#Ejercicio 8
#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

#Ejercicio 9
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

#monto_invertir = float(input('Cantidad a invertir: '))
#tasa_interes = float(input('¿Tasa de retorno?: '))
#year = int(input('¿Por cuantos años?: '))
#ecuacion = round(monto_invertir + (monto_invertir * (tasa_interes/100)) * year, 2)
#print(f'Si invertes {monto_invertir} al {tasa_interes}% de #interes por {year} años Tendras: {ecuacion}')


#Ejercicio 10
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

#peso_payaso = 112
#peso_muñeca = 75
#payaso = int(input('Numero de payasos en el pedido: '))
#muñeca = int(input('Numero de muñecas en el pedido: '))
#pedido = round(payaso * peso_payaso + muñeca * peso_muñeca, 2)
#print(f'El pedido a enviar pesa {pedido/1000}kg')


#Ejercicio 11
#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

# capital_inicial = float(input('Capital inicial: '))
# first_year = round(capital_inicial * (0.04 + 1), 2)
# second_year = round(first_year * (0.04 + 1), 2)
# third_year = round(second_year * (0.04 + 1), 2)
# print(f'Ahorro tras el \n1º Año: {first_year}\n2º Año: {second_year}\n3º Año: {third_year}')


#Ejercicio 12
#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

usuario = int(input('número de barras vendidas que no son del día: '))
pan_dia = 3.49
pan_viejo = 3.49 *(1-0.6), 2
coste = round(usuario * pan_viejo * pan_dia, 2)
print(f'precio habitual ${pan_dia}\ndescuento que se le hace por no ser fresca 60%\ncoste final total ${pan_viejo}')