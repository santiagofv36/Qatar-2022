from Objects.Product import Product

'''
    clase para manejar los restaurantes de los estadios
'''

class Restaurant:

    def __init__(self, name : str):
        self.__name = name
        self.__products = []

    '''
        Getters
    '''

    def getName(self) -> str:
        return self.__name

    def getProducts(self) -> list[Product]:
        return self.__products

    '''
        Setters
    '''

    def setName(self, name) -> None:
        self.__name = name

    def addProducts(self, product) -> None:
        self.__products.append(product)

    '''
        Metodo para imprimir los datos del objeto
    '''

    def __str__(self) -> str:
        products = '\n'.join(str(product)  + '\n' for product in self.__products)
        return f"Nombre: {self.__name} \nProductos:\n\n{products}\n"