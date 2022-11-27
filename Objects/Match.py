from Objects.Stadium import Stadium
from Objects.Team import Team

from datetime import datetime


'''
    Clase Partido para manejar los datos de los partidos
'''

class Match:

    '''
        Inicializador
    '''

    def __init__(self, team1 : Team, team2 : Team, date : datetime, stadium_id: Stadium, id :int) -> None:
        self.__team1 = team1
        self.__team2 = team2
        self.__date = date
        self.__stadium_id = stadium_id
        self.__id = id
        

    '''
        Getters
    '''

    def get_home_team(self) -> str:
        return self.__team1

    def get_away_team(self) -> str:
        return self.__team2

    def getDate(self) -> str:
        return self.__date

    def getTime(self) -> str:
        return self.__time

    def getLocation(self) -> str:
        return self.__location

    def getId(self) -> int:
        return self.__id
    
    def getStadium(self) -> int:
        return self.__stadium_id

    def get_teams(self) -> list:
        return [self.__team1, self.__team2]

    def get_name(self):
        return f"{self.__team1.get_country()} vs {self.__team2.get_country()}"

    '''
        Setters
    '''    

    def setTeam1(self, team1) -> None:
        self.__team1 = team1

    def setTeam2(self, team2) -> None:
        self.__team2 = team2

    def setDate(self, date) -> None:
        self.__date = date

    def setTime(self, time) -> None:
        self.__time = time

    def setLocation(self, location) -> None:
        self.__location = location

    def setId(self, id) -> None:
        self.__id = id
    
    def setStadiumId(self, stadium_id) -> None:
        self.__stadium_id = stadium_id


    '''
        Metodos
    '''

    def __str__(self):
        return f"Partido: {self.__team1.get_country()} vs {self.__team2.get_country()} \nFecha: {self.__date} \nEstadio: {self.__stadium_id.getName()}\n"