with open('./data/day_4_scratch_cards.txt', 'rt') as file:
    cards = file.readlines()
    total = 0
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    for card in cards:
        all_numbers = card.split(":")[1]
        winning_numbers = all_numbers.split("|")[0].strip().split()
        picked_numbers = all_numbers.split("|")[1].strip().split()

        matching_numbers = [x for x in picked_numbers if x in winning_numbers]
        if len(matching_numbers) > 0:
            total += pow(2, len(matching_numbers) - 1)


    print(total)