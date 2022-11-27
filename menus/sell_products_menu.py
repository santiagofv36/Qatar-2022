


def sell_products_menu(clients,stats):


    for i, client in enumerate(clients):
        print(f'{i+1}. {client.get_name()}')
    print('0. Salir')
    op = input('Ingrese el numero del cliente: ')

    if op == '0':
        return

    if not op.isdigit():
        print('Opcion invalida')
        return

    op = int(op)

    if op < 0 or op > len(clients):
        print('Opcion invalida')
        return

    client = clients[op-1]

    ticket = client.getTickets()

        
    match = ticket.get_match()

    stadium = match.getStadium()

    restaurants = stadium.getRestaurants()



    if client.wentToMatch():
        if client.getTickets().get_type() == "VIP":
            for i, restaurant in enumerate(restaurants):
                print(f'{i+1}. {restaurant.getName()}')
            print('0. Salir')

            op = input('Ingrese el numero del restaurante: ')

            if op == '0':
                return

            while not op.isdigit():
                print('Opcion invalida')
                op = input('Ingrese el numero del restaurante: ')

            op = int(op)

            while int(op) < 0 or int(op) > len(restaurants):
                print('Opcion invalida')
                op = input('Ingrese el numero del restaurante: ')

            restaurant = restaurants[int(op)-1]

            products = restaurant.getProducts()
            client_products = []
            '''
                Mientras el cliente quiera seguir comprando
            '''
            while True:
                for i, product in enumerate(products):
                    print(f'{i+1}. {product.getName()}')
                print('0. Pagar')

                op = input('Ingrese el numero del producto: ')

                if op == '0':
                    break

                while not op.isdigit():
                    print('Opcion invalida')
                    op = input('Ingrese el numero del producto: ')

                op = int(op)

                while int(op) < 0 or int(op) > len(products):
                    print('Opcion invalida')
                    op = input('Ingrese el numero del producto: ')

                product = products[int(op)-1]
                client_products.append(product)
                
                if product.getAditional() == "alcoholic":
                    if not client.isLegal():
                        print('No puede comprar este producto debido a su edad')
                        client_products.pop()
                        continue

                    

            total = 0
            subtotal = 0
            discount = "Ninguno"
            # Se resta del inventario
            for product in client_products:
                print(product.getQuantity())
                product.setQuantity(product.getQuantity()-1)

            subtotal = sum(product.getPrice() for product in client_products)
            if client.perfect_number():
                discount = "15%"
                total = subtotal * 0.85
            total = subtotal
            # print the recipe
            print(f"Cliente: {client.get_name()}")
            print(f'Partido: {match.get_home_team().get_country()} vs {match.get_away_team().get_country()}')
            print(f'Estadio: {stadium.getName()}')
            print(f'Restaurante: {restaurant.getName()}')
            print(f'Productos: {", ".join([product.getName() for product in client_products])}')
            print(f'Subtotal: {subtotal}')
            print(f'Descuento: {discount}')
            print(f'Total: {total}')
            client.setExpenses(total)
            stats.addExpense(client)

            input("Presione enter para continuar...")

            
        else:
            print("El cliente no compro un boleto VIP")
            input("Presione enter para continuar...")
            return
    else:
        print("El cliente no fue al partido")
        input("Presione enter para continuar...")
        return




    


    
