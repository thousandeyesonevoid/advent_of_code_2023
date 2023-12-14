# Part 1: 2449062
# Part 2: 33149631

def split_and_convert_to_int(line):
    return [int(x) for x in line.split(":")[1].split()]

total = 1
with open('./data/day_6_boat.txt','r') as file:
    times = split_and_convert_to_int(file.readline())
    distances = split_and_convert_to_int(file.readline())
    
    for index, time in enumerate(times):
        valid_times = []
        distance_to_beat = distances[index]
        # time_charged * (time - time_charged) > d
        for t1 in range(0, time):
            total_distance = t1 * (time - t1)
            if total_distance > distance_to_beat:
                valid_times.append(t1)
        total = total * len(valid_times)

print(total)
