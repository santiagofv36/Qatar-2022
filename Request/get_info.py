from requests import get
from Objects.Team import Team
from Objects.Match import Match
from Objects.Stadium import Stadium
from Objects.Restaurant import Restaurant
from Objects.Product import Product


'''
    Metodo que crea una lista de objetos de tipo Team desde la api 
'''
def create_teams(url: str) ->list[Team]:
    response = get(url)
    teams = []
    if response.status_code == 200:
        for team in response.json():
            t = Team(team['name'], team['fifa_code'], team['group'], team['flag'], team['id'])
            teams.append(t)

    return teams

'''
    Metodo que crea una lista de objetos de tipo Match desde la api
'''
def create_matches(url: str)-> list[Match]:
    response = get(url)
    matches = []
    teams = create_teams('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json')
    stadiums = create_stadiums('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json')
    if response.status_code == 200:
        for match in response.json():
            home_team = next((team for team in teams if team.get_country() == match['home_team']), None)
            away_team = next((team for team in teams if team.get_country() == match['away_team']), None)
            stadium = next((stadium for stadium in stadiums if stadium.getId() == match['stadium_id']), None)
            m = Match(home_team, away_team, match['date'], stadium, match['id'])
            matches.append(m)

    return matches



def create_stadiums(url : str) -> list[Stadium]:
    response = get(url)
    stadiums = []
    if response.status_code == 200:
        for stadium in response.json():
            s = Stadium(stadium['id'], stadium['name'], stadium['capacity'], stadium['location'])
            for restaurant in stadium['restaurants']:
                r = Restaurant(restaurant['name'])
                for product in restaurant['products']:
                    p = Product(product['name'], product['price'], product['type'], product['quantity'], product['adicional'])
                    r.addProducts(p)
                s.addRestaurants(r)
            stadiums.append(s)

    return stadiums