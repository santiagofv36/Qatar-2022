
'''
    Clase para llevar control de todas las estadisticas del programa

'''



from Objects.Client import Client
from Objects.Match import Match
from Objects.Product import Product
from Objects.Stadium import Stadium


class Stats:

    def __init__(self):
        self.__clients = []
        self.__matches = []
        self.__products = []
        self.__stadiums = []
        self.__matches = []
        self.__tickets = {}
        self.__assistants = {}
        self.__totalExpenses = 0


    def initialize(self) -> None:
        for match in self.__matches:
            self.__assistants[match.get_name()] = 0
            self.__tickets[match.get_name()] = 0

    def addClient(self, client : Client) -> None:
        self.__clients.append(client)

    def addMatch(self, match : Match) -> None:
        self.__matches.append(match)

    def addProduct(self, product : Product) -> None:
        self.__products.append(product)

    def addStadium(self, stadium : Stadium) -> None:
        self.__stadiums.append(stadium)

    def addAssistant(self, match, n) -> None:
        self.__assistants[match] += n

    def addTicket(self, match, n) -> None:
        self.__tickets[match] += n

    def addExpense(self, client) -> None:
        print(f"Los gastos del cliente: {client.get_name()} son: {client.getExpenses()}")
        self.__totalExpenses = client.getExpenses()


    def getMatches(self):
        return self.__assistants

    def avgExpenses(self) -> float:
        try:
            vip_clients = [client for client in self.__clients if client.getTickets().get_type() == 'VIP' and client.wentToMatch()]
            return self.__totalExpenses / len(vip_clients)
        except ZeroDivisionError:
            return 0
        

    # order self.__assistants by value from lowest to highest
    def drawTable(self):
        d = self.__assistants
        a = ' '
        print(f"Partido:{a:<20} Asistencia")
        for key, value in sorted(d.items(), key=lambda item: item[1]):
            print(f"{key:<25}    {value:<20}")

    def mostAssistedMatch(self):
        return max(self.__assistants, key=self.__assistants.get)

    def mostSoldTicket(self):
        return max(self.__tickets, key=self.__tickets.get)

    def __str__(self) -> str:
        return f'''
        Estadisticas
        ============
        Clientes: {len(self.__clients)}
        Estadios: {len(self.__stadiums)}
        Partidos: {len(self.__matches)}
        Gastos totales: {self.__totalExpenses}
        Gastos promedio: {self.avgExpenses()}
        '''