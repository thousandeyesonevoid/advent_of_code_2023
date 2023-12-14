import re
import math

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
    
    current_nodes = [node for node in node_index.keys() if node[-1] == 'A' ]
    all_steps = []
    for node in current_nodes:
        next_node = " "
        direction_index = 0
        current_node = node
        steps = 0
        while next_node[-1] != 'Z':
            if next_node != " ":
                current_node = next_node
            direction = directions[direction_index]
            children = node_index[current_node]
            if direction == 'L':
                next_node = children.split(",")[0]
            elif direction == 'R':
                next_node =  children.split(",")[1].strip()
            steps += 1
            direction_index += 1
            if direction_index == len(directions):
                direction_index = 0
        all_steps.append(steps)
    print(math.lcm(*all_steps))