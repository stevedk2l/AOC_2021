from lib import get_input_lines

data = get_input_lines("1.txt", cast_to=int)

greater_than_previous = 0

for x in range(1, len(data)):
    if data[x] > data[x-1]:
        greater_than_previous += 1

print(greater_than_previous)