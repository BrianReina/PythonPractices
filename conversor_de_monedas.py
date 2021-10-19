def conversor(tipo_pesos, valor_dolar):
    pesos = float(input(f'¿Cuántos pesos {tipo_pesos} tienes?: '))
    dolares = round(pesos / valor_dolar, 2)
    print(f'Tienes {dolares} dólares')


if __name__ == '__main__':

    try:
        menu = '''
        Bienvenido al conversor de monedas 💰

        1 - Pesos colombianos
        2 - Pesos argentinos
        3 - Pesos mexicanos

        Elige una opción: '''

        opcion = int(input(menu))

        if opcion == 1:
            conversor('colombianos', 3875)
        elif opcion == 2:
            conversor('argentinos', 65)
        elif opcion == 3:
            conversor('mexicanos', 24)
        else:
            print('Ingresa una opción correcta por favor')

    except ValueError:
        print('¡Solo valores numericos enteros!')