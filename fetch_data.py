import requests

class FetchData:
    '''The Fetch Data class is a wrapper for PokeAPI.'''

    stat_names = ["HP", "ATK", "DEF", "SP. ATK", "SP. DEF", "SPEED"]

    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2"

    def dt_pokemon(self, pokemon: str, response) -> str:
        '''Returns information on a given Pokemon.'''
        
        answer = ""
        total = 0

        data = response.json()['stats']

        print(data)
        answer += "----------------------------------\n"
        answer += f"**{pokemon.title()}**'s stats are as follows: \n"

        for i in range(len(data)):
            answer += f"{FetchData.stat_names[i]}: {data[i]['base_stat']}\n"
            total += data[i]['base_stat']

        answer += f"BST: {total}\n"

        answer += "----------------------------------"
        return answer
    
    def dt_item(self, item: str, response):
        return response.json()['effect_entries'][0]['effect']
    
    def dt_ability(self, ability: str, response):
        pass

    def dt(self, token):

        url = f"{self.base_url}/pokemon/{token}"
        response = requests.get(url)

        if response.status_code == 200:
            return self.dt_pokemon(token, response)
        
        url = f"{self.base_url}/item/{token}"
        response = requests.get(url)

        if response.status_code == 200:
            return self.dt_item(token, response)
        
        return "i don't even know what this is gang try again 😹"