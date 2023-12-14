import re

with open('./data/day_4_scratch_cards.txt', 'rt') as file:
    cards = file.readlines()
    total = 0
    deck = {}
    for card in cards:
        card_number = re.match('Card\s+(\d+):', card).group(1)
        deck[int(card_number)] = [card.split(":")[1]]
    print(deck)
    for card_number, copies in deck.items():
        all_numbers = copies[0]
        winning_numbers = all_numbers.split("|")[0].strip().split()
        picked_numbers = all_numbers.split("|")[1].strip().split()

        matching_numbers = [x for x in picked_numbers if x in winning_numbers]
        for _ in copies:
            for index,_ in enumerate(matching_numbers):
                card_info = deck[card_number + index + 1][0]
                deck[card_number + index + 1].append(card_info)

    for _, copies in deck.items():
        total += len(copies)

    print(total)