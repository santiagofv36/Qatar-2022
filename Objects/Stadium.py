
from Objects.Restaurant import Restaurant
'''
    Clase Estadio para manejar los datos de los estadios
'''

class Stadium:

    '''
        Inicializador
    '''
    def __init__(
        self,
        id : int,
        name : str,
        capacity : list[int],
        location : str,
    ):
        self.__id = id
        self.__name = name
        self.__capacity = capacity
        self.__location = location
        self.__restaurants = []

    
    '''
        Getters
    '''

    def getId(self) -> int:
        return self.__id

    def getName(self) -> str:
        return self.__name

    def getCapacity(self) -> list[int]:
        return self.__capacity

    def getLocation(self) -> str:
        return self.__location

    def getRestaurants(self) -> list[Restaurant]:
        return self.__restaurants

    '''
        Setters
    '''

    def setId(self, id) -> None:
        self.__id = id

    def setName(self, name) -> None:
        self.__name = name

    def setCapacity(self, capacity) -> None:
        self.__capacity = capacity

    def setLocation(self, location) -> None:
        self.__location = location

    '''
        Metodos
    '''

    def addRestaurants(self, restaurant : Restaurant) -> None:
        self.__restaurants.append(restaurant)
    '''
        Metodo que retorna un string con la informacion del estadio
    '''
    def __str__(self) -> str:
        restaurants = ''.join(str(restaurant) + '\n' for restaurant in self.__restaurants)
        return f"ID: {self.__id} \nNombre: {self.__name} \nCapacidad: {self.__capacity} \nUbicacion: {self.__location} \nRestaurantes:\n{restaurants}"