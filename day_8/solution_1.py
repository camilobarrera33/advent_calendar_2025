import math

# Read input
with open('day_8/input.txt', 'r') as f:
    content = f.readlines()

# Remove line break
for i in range(len(content)):
    content[i] = content[i].strip('\n')

# Function to calculate the distance
def calculate_distance(position_matrix, index_1, index_2):
    x_1, y_1, z_1 = position_matrix[index_1].split(',')
    x_2, y_2, z_2 = position_matrix[index_2].split(',')
    return math.sqrt((int(x_2) - int(x_1))**2 + (int(y_2) - int(y_1))**2 + (int(z_2) - int(z_1))**2)


def find_minimum(distance_matrix):
    idx_i = math.inf
    idx_j = math.inf
    min_distance = math.inf
    for i in range(len(distance_matrix)):
        for j in range(len(distance_matrix[i])):
            if (i != j) and (distance[i][j] < min_distance):
                idx_i = i
                idx_j = j
                min_distance = distance_matrix[i][j]
    return idx_i, idx_j, min_distance 

def update_distance_matrix(distance_matrix, idx_1, idx_2):
    distance_matrix[idx_1][idx_2] = math.inf
    distance_matrix[idx_2][idx_1] = math.inf
    return distance_matrix

# Calculate distances between every pair of boxes
distance = [[] for _ in range(len(content))]
for i in range(len(content)):
    for j in range(len(content)):
        distance[i].append(calculate_distance(content, i, j))


circuits = [set() for _ in range(len(content))]
for i in range(len(circuits)):
    circuits[i].add(i)


for i in range(len(content)):
    min_idx_1, min_idx_2, min_value = find_minimum(distance)
    cir_1 = math.inf
    cir_2 = math.inf
    for j in range(len(circuits)):
        if min_idx_1 in circuits[j]:
            cir_1 = j
        if min_idx_2 in circuits[j]:
            cir_2 = j
    if cir_1 != cir_2:
        _temp1 = circuits[cir_1].copy()
        _temp2 = circuits[cir_2].copy()
        circuits.append(circuits[cir_1].union(circuits[cir_2]))
        circuits.remove(_temp1)
        circuits.remove(_temp2)
    distance = update_distance_matrix(distance, min_idx_1, min_idx_2)


circuit_size = [len(i) for i in circuits]
circuit_size.sort(reverse=True)


print(circuit_size[:3])
print(f"Final answer is: {math.prod(circuit_size[:3])}")
