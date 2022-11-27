from Objects.Match import Match

'''
    Clase ticket para manejar las entradas a los partidos
'''


class Ticket:

    '''
        Inicializador
    '''
    def __init__(self, price : float, match : Match, authenticity : bool, type : str):
        self.__price : float = price
        self.__match : Match = match
        self.__authenticity : bool = authenticity
        self.__type : str = type
        self.__used : bool = False


    '''
        getters
    '''

    def get_price(self) -> float:
        return self.__price

    def get_match(self) -> Match:
        return self.__match

    def get_authenticity(self) -> bool:
        return self.__authenticity

    def get_type(self) -> str:
        return self.__type

    def isUsed(self) -> bool:
        return self.__used

    '''
        setters
    '''

    def set_price(self, price : float) -> None:
        self.__price = price

    def set_match(self, match : Match) -> None:
        self.__match = match

    def setUsed(self) -> None:
        self.__used = True

    '''
        Metodos
    '''

    def __str__(self) -> str:
        return f"Ticket:\n Partido: {self.__match} \n Tipo: {self.__type} \n"