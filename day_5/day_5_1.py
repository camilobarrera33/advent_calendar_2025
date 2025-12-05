with open('input.txt', 'r') as file:
    content = file.readlines()

content = [line.strip('\n') for line in content]

ranges = [i for i in content if "-" in i]
ingredients = []

for i in content:
    try:
        int(i)
        ingredients.append(i)
    except:
        pass

fresh_ingredients = 0
for i in ingredients:
    id = int(i)
    for j in ranges:
        lb, ub = j.split("-")
        lb = int(lb)
        ub = int(ub)
        if id >= lb and id <= ub:
            fresh_ingredients += 1
            break
    
print(f"Number of fresh ingredients: {fresh_ingredients}")