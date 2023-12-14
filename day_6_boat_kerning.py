# Part 1: 2449062
# Part 2: 33149631

def split_and_convert_to_int(line):
    value = ''.join(line.split(":")[1].split())
    return int(value)

valid_times = []
with open('./data/day_6_boat.txt','r') as file:
    time = split_and_convert_to_int(file.readline())
    distance = split_and_convert_to_int(file.readline())
    
    for t in range(0, time):
        total_distance = t * (time - t)
        if total_distance > distance:
            valid_times.append(t)

print(len(valid_times))
