import re

digits = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]  
total_calibration = 0

def secondItem(item):
     return item[1]

with open('./data/day_1_trebuchet_data.txt', 'r') as file:
    calibration_content = file.read()
    calibration_rows = calibration_content.split("\n")

    corrected_rows = []
    for row in calibration_rows:
        raw_string = row
        digit_hash = {}
        for digit in digits:
            if digit in row:
                digit_hash[digit] = row.index(digit)

        digit_list = list(digit_hash.items())
        digit_list.sort(key=secondItem)
        for digit, pos in digit_list:
                if digit in raw_string:
                    index = digits.index(digit)
                    digit_length = int(len(digit) / 2)
                    raw_string = raw_string[:pos + digit_length] + str(index + 1) + raw_string[pos+1+digit_length:]
        corrected_rows.append(raw_string)
            
    print(corrected_rows)
    for row in corrected_rows:
        numbers = re.findall(r'\d', row)
        total_calibration += int(f"{numbers[0]}{numbers[-1]}")


print(total_calibration)