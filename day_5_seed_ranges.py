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
            seed_lists = [int(x) for x in line.split(":")[1].split()]
            for index in range (0, int(len(seed_lists)/2)):
                sources.append(
                    {
                        'start': seed_lists[index*2],
                        'range': seed_lists[index*2 + 1]
                    }
                )
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
            for destination in destination_map:
                new_sources = []
                destination_start, source_start, all_range = destination
                for source in sources:
                    first_item = source.get('start')
                    last_item = source.get('start') + source.get('range') - 1
                    if first_item in range(source_start, source_start + all_range):
                        if last_item in range(source_start, source_start + all_range):
                            new_sources.append({
                                'start': destination_start + (first_item - source_start),
                                'range': source.get('range')
                            })
                        else:
                            new_sources.append({
                                'start': destination_start + (first_item - source_start) - 1,
                                'range': all_range
                            })
                            new_sources.append({
                                'start': source_start + all_range,
                                'range': source.get('range') - all_range
                            })
                    elif last_item in range(source_start, source_start + all_range):
                        new_sources.append({
                            'start': source.get('start'),
                            'range': source_start - first_item
                        })
                        new_sources.append({
                            'start': destination_start,
                            'range': last_item - source_start
                        })
                    else:
                        new_sources.append(source)
                sources = new_sources
                # print("------------------")
                print(dest_name)
                # print(destination)
                # print(sources)

    destination_map.sort(key=order_by_second)
    for destination in destination_map:
        new_sources = []
        destination_start, source_start, all_range = destination
        for source in sources:
            first_item = source.get('start')
            last_item = source.get('start') + source.get('range') - 1
            if first_item in range(source_start, source_start + all_range):
                if last_item in range(source_start, source_start + all_range):
                    new_sources.append({
                        'start': destination_start + (first_item - source_start),
                        'range': source.get('range')
                    })
                else:
                    new_sources.append({
                        'start': destination_start + (first_item - source_start) - 1,
                        'range': all_range
                    })
                    new_sources.append({
                        'start': source_start + all_range,
                        'range': source.get('range') - all_range
                    })
            elif last_item in range(source_start, source_start + all_range):
                new_sources.append({
                    'start': source.get('start'),
                    'range': source_start - first_item
                })
                new_sources.append({
                    'start': destination_start,
                    'range': last_item - source_start
                })
            else:
                new_sources.append(source)
        sources = new_sources
    
    print(sources)