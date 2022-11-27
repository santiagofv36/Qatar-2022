
from Objects.Restaurant import Restaurant
from Objects.Seat import Seat
'''
    Clase Estadio para manejar los datos de los estadios
'''

class Stadium:


    '''
        Variables de clase
    '''
    __general_price = 50
    __vip_price = 120


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
        self.__general_seats = [Seat(True, i) for i in range(1, capacity[0]+1)]
        self.__vip_seats = [Seat(True, i) for i in range(1, capacity[1]+1)]
        self.__location = location
        self.__restaurants = []

    
    '''
        Getters
    '''

    def getId(self) -> int:
        return self.__id

    def getName(self) -> str:
        return self.__name

    def getLocation(self) -> str:
        return self.__location

    def getRestaurants(self) -> list[Restaurant]:
        return self.__restaurants

    def getGeneralCapacity(self) -> int:
        return self.__capacity[0]

    def getVipCapacity(self) -> int:
        return self.__capacity[1]

    def getGeneralSeats(self) -> list[Seat]:
        return self.__general_seats

    def getVipSeats(self) -> list[Seat]:
        return self.__vip_seats

    def getGeneralPrice(self) -> int:
        return self.__general_price

    def getVipPrice(self) -> int:
        return self.__vip_price

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
        return f"ID: {self.__id} \nNombre: {self.__name} \nCapacidad: {self.__capacity} \nUbicacion: {self.__location} \n\nRestaurantes:\n{restaurants}\n"


