# import get_info

# Path: Mundial\main.py

from Request.get_info import create_teams, create_matches, create_stadiums

def main():
    teams = create_teams("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json")
    matches = create_matches("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json")
    stadiums = create_stadiums("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json")

    for team in teams:
        print(team)

    for match in matches:
        print(match)

    for stadium in stadiums:
        print(stadium)


'''
    Ejecucion del programa principal
'''
if __name__ == "__main__" :
    main()