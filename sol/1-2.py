from lib import get_input_lines

data = get_input_lines("1.txt", cast_to=int)

greater_than_previous = 0

sliding_sum = []

for x in range(0, len(data) - 1):
    sliding_sum.append(sum(data[x:x+3]))

for y in range(1, len(sliding_sum)):
    if sliding_sum[y] > sliding_sum[y-1]:
        greater_than_previous += 1

print(greater_than_previous)