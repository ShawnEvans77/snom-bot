import pandas
import numpy
from thefuzz import fuzz

class ItemList:
    '''The Item List stores all items from all Pokemon Games.'''

    THRESHOLD = 70

    def __init__(self):
        self.df = pandas.read_csv('assets/items.csv')
        self.list = self.df['identifier'].values.tolist()

    def exists(self, item):
        return item.lower() in self.list
    
    def __contains__(self, item):
        return item.lower() in self.list

    def close_match(self, incorrect) -> str:

        '''Returns the closest match to the input string. Useful for situations where the user mistykes an item.'''

        closest_val = 0
        closest_item = None

        for item in self.list:

            comparison = fuzz.ratio(incorrect.lower(), item)

            if comparison > closest_val and comparison > ItemList.THRESHOLD:
                closest_val = fuzz.ratio(incorrect.lower(), item)
                closest_item = item

        return closest_item