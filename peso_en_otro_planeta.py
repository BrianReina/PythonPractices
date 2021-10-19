def run(dato, planeta):
    GRAVEDAD = 9.807
    peso = float(input('¿Cual es tu peso?: '))
    ecuacion = round((peso / GRAVEDAD) * dato, 2)
    print(f'Tu peso en {planeta} es: {ecuacion}kg')


if __name__ == '__main__':

    try:
        menu = '''
        Selecciona un numero para saber tu peso en otro Planeta

            1- Mercurio
            2- Venus
            3- Marte
            4- Júpiter
            5- Saturno
            6- Urano
            7- Neptuno
        '''
        opcion = int(input(menu))

        #Mercurio
        if opcion == 1:
            run(3.7, 'Mercurio')
        #Venus
        elif opcion == 2:
            run(8.87, 'Venus')
        #Marte
        elif opcion == 3:
            run(3.721, 'Marte')
        #Júpiter
        elif opcion == 4:
            run(24.79, 'Júpiter')
        #Saturno
        elif opcion == 5:
            run(10.44, 'Saturno')
        #Urano
        elif opcion == 6:
            run(8.87, 'Urano')
        #Neptuno
        elif opcion == 7:
            run(11.15, 'Neptuno')
        else:
            print('Ingresa una opcion correcta')

    except ValueError:
        print('Solo se pueden ingresar numeros enteros')