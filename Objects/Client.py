
from Match import Match

from Ticket import Ticket
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
        self.__ticket = None



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


    '''
        setters
    '''

    def set_name(self, name : str) -> None:
        self.__name = name

    def set_id(self, id : str) -> None:
        self.__id = id

    def set_age(self, age : int) -> None:
        self.__age = age

    '''
        Metodos
    '''

    def buyTicket(self, ticket : Ticket) -> None:
        self.__ticket = ticket



