import re

id_total = 0
red_cube_count = 12
green_cube_count = 13
blue_cube_count = 14


with open('./data/day_2_cubes_data.txt', 'r') as file:
    games = file.readlines()

    # Game 1: 12 red, 2 green, 5 blue; 9 red, 6 green, 4 blue; 10 red, 2 green, 5 blue; 8 blue, 9 red
    for game in games:
        game_id = int(re.search('Game (\d+):', game).group(1))
        game_info = game.split(":")[1].split(";")
        valid_info = True
        for info in game_info:
            red_cubes = re.search('(\d+) red', info)
            if red_cubes:
                if int(red_cubes.group(1)) > red_cube_count:
                    valid_info = False
            
            blue_cubes = re.search('(\d+) blue', info)
            if blue_cubes:
                if int(blue_cubes.group(1)) > blue_cube_count:
                    valid_info = False
            
            green_cubes = re.search('(\d+) green', info)
            if green_cubes:
                if int(green_cubes.group(1)) > green_cube_count:
                    valid_info = False
        if valid_info:
            id_total += game_id


print(id_total)
