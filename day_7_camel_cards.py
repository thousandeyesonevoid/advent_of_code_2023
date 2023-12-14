from dataclasses import dataclass
from collections import Counter

value_set = [
    'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'
]

def is_five_of_a_kind(card_counter):
    if len(card_counter) == 1:
        return 100_000_000

def is_four_of_a_kind_or_full_house(card_counter):
    if len(card_counter) == 2:
        if card_counter.most_common(1)[0][1] == 4:
            return 10_000_000
        if card_counter.most_common(1)[0][1] == 3:
            return 1_000_000

def is_3_of_kind_or_2_pair(card_counter):
    if len(card_counter) == 3:
        if card_counter.most_common(1)[0][1] == 3:
            return 100_000
        if card_counter.most_common(1)[0][1] == 2:
            if card_counter.most_common(2)[1][1] == 2:
                return 10_000


def is_one_pair(card_counter):
    if len(card_counter) == 4:
        if card_counter.most_common(1)[0][1] == 2:
            return 1000

        

@dataclass
class Card:
    card:  str
    value: int
    card_value: int = 0

    def set_card_value(self):
        card_counter = Counter(self.card)
        self.card_value = is_five_of_a_kind(card_counter) or is_four_of_a_kind_or_full_house(card_counter) or is_3_of_kind_or_2_pair(card_counter) or is_one_pair(card_counter) or 0

    
    def __lt__(self, other):
        if self.card_value == other.card_value:
            for index, w in enumerate(self.card):
                if w == other.card[index]:
                    continue
                return value_set.index(w) < value_set.index(other.card[index])

        else:
            return self.card_value > other.card_value 
    


with open('./data/day_7_camels.txt','r') as file:
    inputs = file.readlines()
    cards = []
    total = 0
    for input in inputs:
        card, value = input.split()
        card_obj = Card(card=card, value=int(value))
        card_obj.set_card_value()
        cards.append(card_obj)
    
    cards.sort()
    for index, card in enumerate(cards):
        total += (1000 - index) * card.value

    print(total) 
