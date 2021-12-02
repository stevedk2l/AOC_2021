from lib import get_input_lines

data = get_input_lines("2.txt", cast_to=str)

x = 0
y = 0

for z in data:
    unpacked = z.split(" ")
    direction, change = unpacked[0], int(unpacked[1])
    if direction == "forward":
        x += change
    elif direction == "down":
        y -= change
    elif direction == "up":
        y += change

print(x * -y)
