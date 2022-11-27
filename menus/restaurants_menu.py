

from menus.clear_screen import clear_screen


def restaurants_menu(stadiums):
    op = ''
    while op != '0':
        print('''
        ==============================
        |         Estadios           |
        ==============================
        ''')

        for i, stadium in enumerate(stadiums):
            print(f'     {i+1}. {stadium.getName()}')
        print("     0. salir")
        op = input('Ingrese el numero del estadio: ')

        if op == '0':
            return

        try:
            op = int(op)
        except ValueError:
            print("Opcion invalida!")
            input("Presione enter para continuar...")
            return

        if op > len(stadiums) or op < 1:
            print('Opcion invalida!')
            input('Presione enter para continuar...')
            return
        else:
            clear_screen()
            stadium = stadiums[op-1]
            print(f'     Estadio: {stadium.getName()}')
            
            for i, restaurant in enumerate(stadium.getRestaurants()):
                print(f'     {i+1}. {restaurant.getName()}')
            print("     0. salir")
            op2 = input('Ingrese el numero del restaurante: ')

            if op2 == '0':
                return
            
            try:
                op2 = int(op2)
            except ValueError:
                print("Opcion invalida!")
                input("Presione enter para continuar...")
                return

            if op2 > len(stadium.getRestaurants()) or op2 < 1:
                print('Opcion invalida!')
                input('Presione enter para continuar...')
                return
            else:
                clear_screen()
                restaurant = stadium.getRestaurants()[op2-1]
                actions_menu(restaurant)



    input('Presione enter para continuar...')


def search_by_name(restaurant):
    clear_screen()
    print(f"     Restaurante: {restaurant.getName()}")
    print('''
    ===========================================
    |         Buscar producto por nombre      |
    ===========================================
    ''')
    name = input('Ingrese el nombre del producto: ')
    clear_screen()
    print(f"     Buscando productos con el nombre: {name} en el restaurante {restaurant.getName()}")
    for product in restaurant.getProducts():
        if name == product.getName().lower():
            print(f' {product}')
    input("Presione enter para continuar...")

def search_by_price(restaurant):

    clear_screen()
    print(f"     Restaurante: {restaurant.getName()}")
    print('''
    ===========================================
    |         Buscar producto por precio      |
    ===========================================
    ''')
    min_price = input('Ingrese el precio minimo: ')
    max_price = input('Ingrese el precio maximo: ')
    clear_screen()
    print(f"     Buscando productos con el precio entre {min_price} y {max_price} en el restaurante {restaurant.getName()}")
    try:
        min_price = float(min_price)
        max_price = float(max_price)
    except ValueError:
        print("Solo se permiten numeros!")
        input("Presione enter para continuar...")
        return
    for i,product in enumerate(restaurant.getProducts()):
        if product.getPrice() >= min_price and product.getPrice() <= max_price:
            print(f' {i+1}. \n{product}')
            print()
    input("Presione enter para continuar...")


def search_by_category(restaurant):
    clear_screen()
    print(f"     Restaurante: {restaurant.getName()}")
    print('''
    =========================================
    |       Buscar producto por categoria   |
    =========================================
    | 1.- Bebidas                           |
    | 2.- Comida                            |
    =========================================
    ''')
    op = input('Ingrese el numero de la categoria: ')
    if op == '1':
        category = 'beverages'
    elif op == '2':
        category = 'food'
    else:
        print("Opcion invalida!")
        input("Presione enter para continuar...")
        return
    clear_screen()
    print(f"     Buscando productos de la categoria: {category} en el restaurante {restaurant.getName()}")
    for i,product in enumerate(restaurant.getProducts()):
        if category == product.getType():
            print(f' {i+1}. \n{product}')
            print()
    input("Presione enter para continuar...")



def actions_menu(restaurant):
    print(f"     Restaurante: {restaurant.getName()}")
    print('''
    ===========================================
    |               Acciones                  |
    ==========================================|
    | 1.- Buscar producto por nombre          |
    | 2.- Buscar producto por rango de precio |
    | 3.- Buscar producto por categoria       |
    | 0.- Salir                               |
    ===========================================
    ''')
    op = input('Ingrese el numero de la accion: ')

    if op == '1':
        search_by_name(restaurant)
    elif op == '2':
        search_by_price(restaurant)
    elif op == '3':
        search_by_category(restaurant)
    elif op == '0':
        return
    else:
        print("Opcion invalida!")
        input("Presione enter para continuar...")
        return
