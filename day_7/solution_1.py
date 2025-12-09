# Read input
with open('day_7/input.txt', 'r') as f:
    content = f.readlines()

for i in range(len(content)):
    content[i] = content[i].strip('\n')

# Find the index where the letter 'S' is in the first line
first_line = content[0]
for i in range(len(first_line)):
    if first_line[i] == 'S':
        idx = i
        break
print(f"S found at index {idx}")

# Start projecting down the beam
beam = {idx: 1}
split_count = 0
for i in range(len(content[1:])):
    dict_keys = list(beam.keys())
    for j in dict_keys:
        if content[i][j] == '^':
            beam[j-1] = 1
            beam[j+1] = 1
            beam.pop(j)
            split_count += 1

print(f"Final answer {split_count}")