# Read input data
with open("day_9/input.txt", "r") as f:
    content = f.readlines()

content = [i.strip("\n") for i in content]
content = [i.split(',') for i in content]
print(f"Data loaded. There are {len(content)} rows in the input")

max_area = 0
max_x_1 = 0
max_x_2 = 0
max_y_1 = 0
max_y_2 = 0
for i in range(len(content) - 1):
    for j in range(i, len(content)):
        x_1 = int(content[i][1])
        y_1 = int(content[i][0])
        x_2 = int(content[j][1])
        y_2 = int(content[j][0])
        x_distance = abs(x_1 - x_2) + 1
        y_distance = abs(y_1 - y_2) + 1
        area = x_distance * y_distance
        if area > max_area:
            max_area = area
            max_x_1 = x_1
            max_x_2 = x_2
            max_y_1 = y_1
            max_y_2 = y_2

print(f"Final anwser: {max_area}")
print(f"Foun at coordinates [{max_y_1}, {max_x_1}] and [{max_y_2}, {max_x_2}]")