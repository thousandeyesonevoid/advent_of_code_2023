import re

symbols = ['+', '=', '/', '#', '%', '$', '-', '@', '&', '*']

with open('./data/day_3_missing_engine_data.txt', 'r') as file:
    rows = file.readlines()
    valid_numbers = []
    for i, row in enumerate(rows):
        for j, character in enumerate(row):
            if character == '.':
                continue
            if character == '*':
                possible_positions = [
                    (i,j-1),
                    (i,j+1),
                    (i-1,j),
                    (i-1,j-1),
                    (i-1,j+1),
                    (i+1,j),
                    (i+1,j-1),
                    (i+1,j+1)
                ]
                surrounding_numbers_by_row = {}
                for x,y in possible_positions:
                    if x < 0 or (x > len(rows) - 1) or (y > len(row) - 1) or y < 0:
                        continue
                    
                    if not re.match(r'\d', rows[x][y]):
                        continue
                    
                    sub_row = rows[x]
                    surrounding_numbers = surrounding_numbers_by_row.get(x, [])
                    all_numbers = re.finditer('\d+', sub_row)
                    for number in all_numbers:
                        if y in range(number.start(0), number.end(0)):
                            surrounding_numbers.append(number.group(0))
                    
                    surrounding_numbers_by_row[x] = list(set(surrounding_numbers))
                part_numbers = []         
                for number_list in surrounding_numbers_by_row.values():
                    part_numbers += number_list
                 
                if len(part_numbers) == 2:
                  valid_numbers.append(int(part_numbers[0]) * int(part_numbers[1]))
    
    total = 0
    for number in valid_numbers:
        total += number

    print(total)



    