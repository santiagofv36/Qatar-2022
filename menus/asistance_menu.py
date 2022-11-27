

from menus.clear_screen import clear_screen


def asistance_menu(clients,stats):

    print('''
    =========================================
    |        Asistencia a los partidos      |
    =========================================
    ''')

    for i in range(len(clients)):
        print(f"{i+1}. {clients[i].get_name()}")

    op = input('Ingrese el numero del cliente: ')

    while op not in [str(i) for i in range(1,len(clients)+1)]:
        print("Opcion invalida!")
        input("Presione enter para continuar...")
        op = input("Ingrese el numero del cliente: ")

    client = clients[int(op)-1]

    assist(client,stats)


def assist(client,stats):

    op = ''
    while op != '0':
        clear_screen()
        print('''
        ==============================
        |      Menu de asistencia    |
        ==============================
        | 1. Asistir a partido       |
        | 0. Salir                   |
        ==============================
        ''')

        op = input("Ingrese una opcion: ")
        if op == "1":
            
            if not client.getTickets():
                print("El cliente no tiene boletos")
                input("Presione enter para continuar...")
                return

            ticket = client.getTickets()

            if not ticket.get_authenticity():
                print("El boleto no es autentico!")
                input("Presione enter para continuar...")
                return

            if ticket.isUsed():
                print("Este boleto ya fue utilizado!")

            else:
                ticket.setUsed()
                client.setWent()
                match = ticket.get_match().get_name()
                stats.addAssistant(match, 1)
                print("Boleto utilizado!")
            input("Presione enter para continuar...")