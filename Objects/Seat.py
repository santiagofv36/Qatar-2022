

class Seat:

    def __init__(self, available : bool, position : int) -> None:
        self.__available = available
        self.__position = position

    def isAvailable(self) -> bool:
        return self.__available

    def getPosition(self) -> int:
        return self.__position

    def setAvailable(self, available : bool) -> None:
        self.__available = available

    def setPosition(self, position : int) -> None:
        self.__position = position

    def __str__(self) -> str:
        return f"Posicion: {self.__position}, Disponible: {self.__available}"

    