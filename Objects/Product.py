
'''
    Clase para manejar los objetos de tipo producto de los estadios
'''


class Product:

    '''
        Inicializador
    '''

    def __init__(self, name : str, price : float, type : str, quantity : int, aditional : str):
        self.__name = name
        self.__price = price
        self.__type = type
        self.__quantity = quantity
        self.__aditional = aditional

    '''
        Getters
    '''

    def getName(self) -> str:
        return self.__name

    def getPrice(self) -> float:
        return self.__price

    def getType(self) -> str:
        return self.__type

    def getQuantity(self) -> int:
        return self.__quantity

    def getAditional(self) -> str:
        return self.__aditional

    '''
        Setters
    '''

    def setName(self, name) -> None:
        self.__name = name

    def setPrice(self, price) -> None:
        self.__price = price

    def setType(self, type) -> None:
        self.__type = type

    def setQuantity(self, quantity) -> None:
        self.__quantity = quantity

    def setAditional(self, aditional) -> None:
        self.__aditional = aditional

    '''
        Metodo para imprimir los datos del objeto
    '''

    def __str__(self) -> str:
        return f"Nombre: {self.__name}\n Precio: {self.__price}\n Tipo: {self.__type}\n Cantidad: {self.__quantity}\n Aditional: {self.__aditional}"