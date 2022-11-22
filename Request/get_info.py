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
    if response.status_code == 200:
        for match in response.json():
            m = Match(match['home_team'], match['away_team'], match['date'], match['stadium_id'], match['id'])
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
                    p = Product(product['name'], product['price'], product['type'])
                    r.addProducts(p)
                s.addRestaurants(r)
            stadiums.append(s)

    return stadiums