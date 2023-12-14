import re

sources = []
destination_map = []
dest_name = ''

def order_by_second(x):
    return x[1]



with open('./data/day_5_seed_location.txt','rt') as file:
    lines = file.readlines()
    for line in lines:
        if 'seeds' in line:
            sources = [int(x) for x in line.split(":")[1].split()]
            continue

        if 'map' in line:
            destination_map = []
            dest_name = line
            continue

        if re.match('\d+', line):
            destination_map.append([ int(x) for x in line.split() ])
            continue

        if line.strip() == '' and destination_map:
            destination_map.sort(key=order_by_second)
            for source in sources:
                new_source = source
                for destination in destination_map:
                    destination_start, source_start, all_range = destination
                    if source in range(source_start, source_start + all_range):
                        new_source = destination_start + (source - source_start)
                sources[sources.index(source)] = new_source

    for source in sources:
        new_source = source
        for destination in destination_map:
            destination_start, source_start, all_range = destination
            if source in range(source_start, source_start + all_range):
                new_source = destination_start + (source - source_start)
        sources[sources.index(source)] = new_source
    print(min(sources))