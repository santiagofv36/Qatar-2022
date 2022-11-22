from Match import Match

'''
    Clase ticket para manejar las entradas a los partidos
'''


class Ticket:

    '''
        Inicializador
    '''
    def __init__(self, type : str, price : float, match : Match, authenticity : bool):
        self.__type : str = type
        self.__price : float = price
        self.__match : Match = match
        self.__authenticity : bool = authenticity


    '''
        getters
    '''

    def get_type(self) -> str:
        return self.__type

    def get_price(self) -> float:
        return self.__price

    def get_match(self) -> Match:
        return self.__match

    def get_authenticity(self) -> bool:
        return self.__authenticity

    '''
        setters
    '''

    def set_tipo(self, tipo : str) -> None:
        self.__tipo = tipo

    def set_price(self, price : float) -> None:
        self.__price = price

    def set_match(self, match : Match) -> None:
        self.__match = match

    '''
        Metodos
    '''

    def __str__(self) -> str:
        return f"Tipo: {self.__tipo} \nPrecio: {self.__price} \nPartido: {self.__match.printMatch()}"