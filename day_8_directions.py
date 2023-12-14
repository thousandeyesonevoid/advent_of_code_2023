import re

with open('./data/day_8_directions.txt', 'r') as file:
    directions = file.readline().strip()
    file.readline()
    nodes = file.readlines()
    steps = 0

    direction_index = 0
    node_index = {}
    for node in nodes:
        root = node.split("=")[0].strip()
        children = node.split("=")[1].strip()
        node_index[root] = re.search('\w+, \w+', children).group(0)
    
    next_node = ""
    current_node = "AAA"
    while next_node != "ZZZ":
        if next_node != '':            
            current_node = next_node
        children = node_index[current_node]
        direction = directions[direction_index]
        if direction == 'L':
            next_node = children.split(",")[0]
        elif direction == 'R':
            next_node =  children.split(",")[1].strip()
        steps += 1
        direction_index += 1
        if direction_index == len(directions):
            direction_index = 0
    
    print(steps)