import re

total_calibration = 0

with open('./data/day_1_trebuchet_data.txt', 'r') as file:
    calibration_content = file.read()
    calibration_rows = calibration_content.split("\n")

    for row in calibration_rows:
        numbers = re.findall(r'\d', row)
        total_calibration += int(f"{numbers[0]}{numbers[-1]}")


print(total_calibration) # 53080