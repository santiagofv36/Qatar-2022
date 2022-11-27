
from Objects.Match import Match


from Objects.Ticket import Ticket
import itertools as it

'''
    Clase cliente para manejar los datos de los clientes
'''

class Client:
    
    '''
        Inicializador
    '''

    def __init__(self,name: str, id : str, age: int):
        self.__name : str = name
        self.__id : str = id
        self.__age : int = age
        self.__ticket : Ticket = None
        self.__went : bool = False
        self.__expenses : float = 0

    '''
        getters
    '''

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> str:
        return self.__id

    def get_age(self) -> int:
        return self.__age

    def get_match(self) -> Match:
        return self.__ticket

    def getTickets(self) -> Ticket:
        return self.__ticket

    def wentToMatch(self) -> bool:
        return self.__went

    def getExpenses(self) -> float:
        return self.__expenses

    '''
        setters
    '''

    def set_name(self, name : str) -> None:
        self.__name = name

    def set_id(self, id : str) -> None:
        self.__id = id

    def set_age(self, age : int) -> None:
        self.__age = age

    def setWent(self) -> None:
        self.__went = True

    def setExpenses(self, expenses : float) -> None:
        self.__expenses += expenses

    '''
        Metodos
    '''

    def buyTicket(self, ticket : Ticket) -> None:
        self.__ticket = ticket

    def buyProduct(self, amount) -> None:
        self.__expenses += amount

    def __str__(self) -> str:
        return f'Nombre: {self.__name} \nCedula: {self.__id} \nEdad: {self.__age}'

    '''
        funcion que obtiene los colmillos del numero
    '''
    def getFangs(self):
        num_iter = it.permutations(self.__id, len(self.__id))
        for num_list in num_iter:
            
            v = ''.join(num_list)
            x, y = v[:int(len(v)/2)], v[int(len(v)/2):]

            if x[-1] == '0' and y[-1] == '0':
                continue


            if int(x) * int(y) == int(self.__id):
                return x,y
        return False

    '''
        Metodo que dice si la cedula es un numero vampiro
    '''
    def isVampire(self):

        n_str = str(self.__id)

        if len(n_str) % 2 == 1:
            return False

        fangs = self.getFangs()
        return bool(fangs)

    def perfect_number(self)-> bool:
        return sum(i for i in range(1, int(self.__id)) if int(self.__id) % i == 0) == int(self.__id)

    def isLegal(self) -> bool:
        return int(self.__age) >= 18

