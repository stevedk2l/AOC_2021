from lib import get_input_lines

data = get_input_lines("2.txt", cast_to=str)

x = 0
aim = 0
depth = 0

for z in data:
    unpacked = z.split(" ")
    direction, change = unpacked[0], int(unpacked[1])
    if direction == "forward":
        x += change
        depth += (change * aim)
    elif direction == "down":
        aim += change
    elif direction == "up":
        aim -= change

print(x * depth)