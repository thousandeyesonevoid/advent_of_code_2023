import re

pow_set_total = 0

with open('./data/day_2_cubes_data.txt', 'r') as file:
    games = file.readlines()

    # Game 1: 12 red, 2 green, 5 blue; 9 red, 6 green, 4 blue; 10 red, 2 green, 5 blue; 8 blue, 9 red
    for game in games:
        min_red, min_blue, min_green = (0,0,0)
        game_info = game.split(":")[1].split(";")
        for info in game_info:
            red_cubes = re.search('(\d+) red', info)
            if red_cubes:
                if int(red_cubes.group(1)) > min_red:
                    min_red = int(red_cubes.group(1))
            
            blue_cubes = re.search('(\d+) blue', info)
            if blue_cubes:
                if int(blue_cubes.group(1)) > min_blue:
                    min_blue = int(blue_cubes.group(1))
            
            green_cubes = re.search('(\d+) green', info)
            if green_cubes:
                if int(green_cubes.group(1)) > min_green:
                    min_green = int(green_cubes.group(1))
        pow_set_total += (min_red * min_blue * min_green)
                

print(pow_set_total)
