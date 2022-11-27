from Objects.stats import Stats
from Request.get_info import create_teams, create_matches, create_stadiums
from generate.generate_clients import generate_clients
from menus.asistance_menu import asistance_menu
from menus.clear_screen import clear_screen
from menus.stats_menu import stats_menu
from menus.teams_menu import team_menu
from menus.sales_menu import sales_menu
from menus.sell_products_menu import sell_products_menu
from menus.restaurants_menu import restaurants_menu


'''
    obtencion de datos de la api
'''

teams = create_teams("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json")
matches = create_matches("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json")
stadiums = create_stadiums("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json")

'''
    Creacion de las estadisticas
'''

def load_stats(clients, stadiums, matches):

    stats = Stats()
    for client in clients:
        stats.addClient(client)

    for stadium in stadiums:
        stats.addStadium(stadium)

    for match in matches:
        stats.addMatch(match)
    
    stats.initialize()

    return stats

'''
    Menu principal
'''
def main_menu():
    op = ''
    # clients = generate_clients(10, matches)
    clients = []
    stats = load_stats(clients, stadiums, matches)

    while op != '0':
        clear_screen()
        print('''
        =========================================
        |               Mundial                 |
        =========================================
        | 1. Partidos y estadios                |
        | 2. Venta de entradas                  |
        | 3. Asistencia a los partidos          |
        | 4. Restaurantes                       |
        | 5. Venta de productos en restaurantes |
        | 6.- Estadisticas                      |
        | 0. Salir                              |
        =========================================
        ''')
        op = input('Ingrese una opcion: ')

        if op == '1':
            team_menu(teams,matches,stadiums)
        elif op == '2':
            client = sales_menu(matches,stats)
            clients.append(client)
        elif op == '3':
            asistance_menu(clients,stats)

        elif op == '4':
            restaurants_menu(stadiums)
            
        elif op == '5':
            sell_products_menu(clients,stats)
        
        elif op == '6':
            stats_menu(stats)

        elif op == '0':
            print('Hasta pronto!')
        else:
            print('Opcion invalida!')
            input('Presione enter para continuar...')