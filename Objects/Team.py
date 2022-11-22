
'''
    Clase Equipo para manejar los datos de los equipos
'''

class Team:
    
    def __init__(self, country: str, FIFA_ID : int, group : str, flag, id : int) -> None:
        self.__country : str = country
        self.__FIFA_ID : int = FIFA_ID
        self.__group : str = group
        self.__flag = flag
        self.__id = id

    '''
        getters
    '''

    def get_country(self) -> str:
        return self.__country

    def get_FIFA_ID(self) -> str:
        return self.__FIFA_ID

    def get_group(self) -> str:
        return self.__group

    def get_flag(self):
        return self.__flag

    def get_id(self):
        return self.__id

    '''
        setters
    '''

    def set_country(self, country: str) -> None:    
        self.__country = country

    def set_FIFA_ID(self, FIFA_ID: str) -> None:
        self.__FIFA_ID = FIFA_ID

    def set_group(self, group: str) -> None:
        self.__group = group

    def set_flag(self, flag) -> None:
        self.__flag = flag

    '''
        Metodos
    '''

    '''
        Metodo que retorna un string con la informacion del equipo
    '''
    def __str__(self)-> str:
        return f"Pais: {self.__country}\nID: {self.__FIFA_ID}\nGrupo: {self.__group}\nBandera: {self.__flag}\nID: {self.__id}\n"
