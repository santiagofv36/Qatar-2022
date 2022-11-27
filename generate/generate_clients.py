


import random

from Objects.Client import Client
from Objects.Ticket import Ticket


'''
    Metodo que crea 10 clientes al azar y les asgina un ticket falso
'''


def generate_clients( n, matches)-> list[Client]:

    clients = []
    names = ['Juan', 'Pedro', 'Maria', 'Jose', 'Luis', 'Ana', 'Luisa', 'Carlos', 'Rosa', 'Ramon', 'Miguel', 'Sofia', 'Sara', 'Laura', 'Pablo', 'Alejandro', 'Fernando', 'Jorge', 'Mariana', 'Diana']

    ids = [random.randint(10000000,99999999) for _ in range(20)]

    ages = [random.randint(5,60) for _ in range(20)]

    category = {'General': 50.0, 'VIP': 120.0}



    for _ in range(n):

        name = random.choice(names)
        _id = random.choice(ids)
        age = random.choice(ages)
        _type, price = random.choice(list(category.items()))
        client = Client(name, _id, age)
        match = random.choice(matches)
        ticket = Ticket(price, match,False,_type)
        client.buyTicket(ticket)
        clients.append(client)
        

    return clients




