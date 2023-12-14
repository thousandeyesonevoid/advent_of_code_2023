from dataclasses import dataclass
from collections import Counter

value_set = [
    'A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'
]

cv_hash = { 'five_of_kind': 100_000_000,
'four_of_kind': 10_000_000,
'full_house': 1_000_000,
'three_of_kind': 100_000,
'two_pair': 10_000,
'pair': 1000}

def check_card_hand(cards):
    card_counter = Counter(cards)
    card_counter_without_j = Counter(cards)
    j_card_count = card_counter_without_j['J']
    del card_counter_without_j['J']
    if len(card_counter) == 1:
        return 'five_of_kind'
    if len(card_counter) == 2:
        if card_counter_without_j.most_common(1)[0][1] == 4:
            if j_card_count == 1:
                return 'five_of_kind'
            return 'four_of_kind'
        if card_counter_without_j.most_common(1)[0][1] == 3:
            if j_card_count == 2:
                return 'five_of_kind'
            return 'full_house'
        if card_counter_without_j.most_common(1)[0][1] == 2:
            if j_card_count == 3:
                return 'five_of_kind'
        if j_card_count == 4:
            return 'five_of_kind'
    if len(card_counter) == 3:
        if card_counter_without_j.most_common(1)[0][1] == 3:
            if j_card_count == 1:
                return 'four_of_kind'
            return 'three_of_kind'
        if card_counter_without_j.most_common(1)[0][1] == 2:
            if j_card_count == 2:
                return 'four_of_kind'
            if card_counter_without_j.most_common(2)[1][1] == 2:
                if j_card_count == 1:
                    return 'full_house'      
                return 'two_pair'
        if j_card_count == 3:
            return 'four_of_kind'
    if len(card_counter) == 4:
        if card_counter_without_j.most_common(1)[0][1] == 2:
            if j_card_count == 1:
                return 'three_of_kind'
            return 'pair'
        if j_card_count == 2:
            return 'three_of_kind'
    if j_card_count == 1:
        return 'pair'
            
            
@dataclass
class Card:
    card:  str
    value: int
    card_value: int = 0

    def set_card_value(self):
        card_value = check_card_hand(self.card)
        print(f"{card_value} for {self.card}")
        self.card_value = cv_hash.get(card_value, 0)

    
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
