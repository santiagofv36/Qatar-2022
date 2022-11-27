
from menus.clear_screen import clear_screen

'''
    Funcion que muestra todos los partidos de un pais
'''

def all_matches_by_country(teams,matches):
    clear_screen()

    op = ''
    while op != '0':
        clear_screen()
        print('''Paises''')

        for i, team in enumerate(teams):
            print(f'{i+1}. {team.get_country()}')
        print("0. salir")
        op = input('Ingrese el numero del equipo: ')

        if op == '0':
            break


        try:
            op = int(op)
        except ValueError:
            print("Opcion invalida!")
            input("Presione enter para continuar...")
            return

        if op > len(teams) or op < 1:
            print('Opcion invalida!')
            input('Presione enter para continuar...')
            continue
        else:
            clear_screen()
            print(f'Partidos de {teams[op-1].get_country()}')
            for match in matches:
                if teams[op - 1].get_country() in [match.get_home_team().get_country(), match.get_away_team().get_country()]:
                    print(match)
            input('Presione enter para continuar...')
            break



def all_matches_by_stadium(matches,stadiums):
    clear_screen()

    op = ''
    while op != '0':
        clear_screen()
        print('''Estadios''')

        for i, stadium in enumerate(stadiums):
            print(f'{i+1}. {stadium.getName()}')
        print("0. salir")
        op = input('Ingrese el numero del estadio: ')

        if op == '0':
            break
        try:
            op = int(op)
        except ValueError:
            print("Opcion invalida!")
            input("Presione enter para continuar...")
            return
        if op > len(stadiums) or op < 1:
            print('Opcion invalida!')
            input('Presione enter para continuar...')
            continue
        else:
            clear_screen()
            print(f'Partidos en {stadiums[op-1].getName()}')
            for match in matches:
                if stadiums[op - 1].getId() == match.getStadium().getId():
                    print(match)
            input('Presione enter para continuar...')
            break

def all_matches_by_date(matches):
    clear_screen()
    op = ''
    while op != '0':
        clear_screen()
        print('''Fechas''')

        dates = []
        for match in matches:
            if match.getDate() not in dates:
                dates.append(match.getDate())

        for i, date in enumerate(dates):
            print(f'{i+1}. {date}')
        print("0. salir")
        op = input('Ingrese el numero de la fecha: ')

        if op == '0':
            break

        try:
            op = int(op)
        except ValueError:
            print("Opcion invalida!")
            input("Presione enter para continuar...")
            return
        if op > len(dates) or op < 1:
            print('Opcion invalida!')
            input('Presione enter para continuar...')
            continue
        else:
            clear_screen()
            print(f'Partidos de {dates[op-1]}')
            for match in matches:
                if dates[op - 1] == match.getDate():
                    print(match)
            input('Presione enter para continuar...')
            break


def team_menu(teams,matches,stadiums):
    op = ''

    while op != '0':
        clear_screen()
        print('''
        =========================================
        |      Gestión de equipos y partidos    |
        =========================================
        | 1. Todos los partidos de un pais      |
        | 2. Todos los partidos de un estadio   |
        | 3. Todos los partidos en una fecha    |
        | 0. Volver                             |
        =========================================
        ''')
        op = input('Ingrese una opcion: ')

        if op == '1':
            all_matches_by_country(teams,matches)
        elif op == '2':
            all_matches_by_stadium(matches,stadiums)
        elif op == '3':
            all_matches_by_date(matches)

        elif op == '0':
            return
        else:
            print('Opcion invalida!')
            input('Presione enter para continuar...')