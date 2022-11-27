
from Objects.Client import Client
from Objects.Ticket import Ticket
from menus.clear_screen import clear_screen



'''
    Funcion que colecciona los datos del cliente y los almacena en un objeto
'''
def register_client() -> Client:
    clear_screen()
    _id = ''
    age = ''
    print('''
    ==============================
    |     Registro de cliente    |
    ==============================
    ''')
    name = input("Ingrese su nombre: ")
    while not _id.isdigit():
        _id = input("Ingrese su cedula: ")
        if _id.isdigit():
            break
        print("Cedula invalida!")
    while not age.isdigit():
        age = input("Ingrese su edad: ")
        if age.isdigit():
            break
        print("Edad invalida!")

    return Client(name,_id, age)


'''
    Metodo que muestra los puestos del estadio
'''

def show_stadium_layout(stadium ,client : Client,match,flag,stats):

    seats = stadium.getGeneralSeats() if flag else stadium.getVipSeats()
    capacity = stadium.getGeneralCapacity() if flag else stadium.getVipCapacity()
    price = stadium.getGeneralPrice() if flag else stadium.getVipPrice()
    _type = "General" if flag else "VIP"
    total = 0
    subtotal = 0
    descuento = ''

    clear_screen()
    print('''
    ==============================
    |    Seleccion de puestos    |
    ==============================
    ''')

    for i in range(1, capacity+1):
        if i % 10 == 0:
            print(i)
        elif i < 10:
            print(f"0{i}", end=' ')
        else:
            print(i, end=' ')

    op = input('Seleccione un puesto: ')

    while op not in [str(i) for i in range(1,capacity+1)]:
        print("Opcion invalida!")
        input("Presione enter para continuar...")
        op = input('Seleccione un puesto: ')

    # check if the seat is available
    if seats[int(op)-1].isAvailable():

        if client.isVampire():
            price*=  0.5
            descuento = '50%'
        
        subtotal = price

        total = subtotal * 1.16

        print("Detalle de la compra")
        print(f"Cliente: {client.get_name()}")
        print(f'Partido: {match.get_home_team().get_country()} vs {match.get_away_team().get_country()}')
        print(f'Puesto: {str(op)}')
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Descuento: {descuento}")
        print(f"Total: {total:.2f}")

        ticket = Ticket(total, match, True, _type)
        client.setExpenses(total)
        stats.addClient(client)
        if _type == "VIP":
            stats.addExpense(client)

        client.buyTicket(ticket)
        stats.addTicket(ticket.get_match().get_name(),1)

        seats[int(op)-1].setAvailable(False)

    else:
        print('El puesto no esta disponible')


    input("Presione enter para continuar...")


def sales_menu(matches,stats):
    client = register_client()

    op = ''
    while op not in {'1','2'}:
        clear_screen()
        print('''
        ==============================
        |         Menu de ventas     |
        ==============================
        | 1. Comprar boleto general  |
        | 2. Comprar boleto VIP      |
        ==============================
        ''')

        op = input("Ingrese una opcion: ")

        if op == "1":
            for i, match in enumerate(matches):
                print(f"{i+1}. {match}")

            op2 = input("Ingrese el numero del partido: ")

            while op2 not in [str(i) for i in range(1,len(matches)+1)]:
                print("Opcion invalida!")
                input("Presione enter para continuar...")
                op2 = input("Ingrese el numero del partido: ")

            match = matches[int(op2)-1]
            stadium = match.getStadium()
            show_stadium_layout(stadium,client,match, True,stats)
            break
        elif op == "2":
            for i, match in enumerate(matches):
                print(f"{i+1}. {match}")

            op2 = input("Ingrese el numero del partido: ")

            while op2 not in [str(i) for i in range(1,len(matches)+1)]:
                print("Opcion invalida!")
                input("Presione enter para continuar...")
                op2 = input("Ingrese el numero del partido: ")

            match = matches[int(op2)-1]
            stadium = match.getStadium()
            show_stadium_layout(stadium,client,match, False,stats)
            break
        else:
            print("Opcion invalida!")
            input("Presione enter para continuar...")
            clear_screen()
    return client