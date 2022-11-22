
'''
    Clase para manejar los objetos de tipo producto de los estadios
'''


class Product:

    '''
        Inicializador
    '''

    def __init__(self, name : str, price : float, type : str):
        self.__name = name
        self.__price = price
        self.__type = type

    '''
        Getters
    '''

    def getName(self) -> str:
        return self.__name

    def getPrice(self) -> float:
        return self.__price

    def getType(self) -> str:
        return self.__type

    '''
        Setters
    '''

    def setName(self, name) -> None:
        self.__name = name

    def setPrice(self, price) -> None:
        self.__price = price

    def setType(self, type) -> None:
        self.__type = type

    '''
        Metodo para imprimir los datos del objeto
    '''

    def __str__(self) -> str:
        return f"Nombre: {self.__name} \nPrecio: {self.__price} \nTipo: {self.__type}"