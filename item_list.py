import pandas
import numpy
from thefuzz import fuzz

class ItemList:

    def __init__(self):
        self.df = pandas.read_csv('items.csv')
        self.list = self.df['identifier'].values.tolist()

    def exists(self, pokemon):
        return pokemon.lower() in self.list
    
    def __contains__(self, pokemon):
        return pokemon.lower() in self.list

    def close_match(self, incorrect):
        closest = [item for item in self.list if fuzz.ratio(incorrect.lower(), item) >= 65]
        return closest