# Read input data
with open("day_10/example_input.txt", "r") as f:
    content = f.readlines()

content = [i.strip("\n") for i in content]

content = [i.split(" ") for i in content]

indicator_lights = []
buttons = [[] for i in content]

for i in range(len(content)):
    for j in content[i]:
        if j[0] == "[":
            indicator_lights.append(j.strip("[]"))
        elif j[0] == "(":
            buttons[i].append(j.strip("()").split(","))

for i in indicator_lights:
    light_index = []
    for j in range(len(i)):
        if i[j] == '#':
            light_index.append(j)
    



