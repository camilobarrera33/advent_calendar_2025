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

fresh_ranges = []
for i in ingredients:
    id = int(i)
    for j in ranges:
        lb, ub = j.split("-")
        lb = int(lb)
        ub = int(ub)
        if id >= lb and id <= ub:
            fresh_ranges.append(str(lb) + "-" + str(ub))

fresh_ranges = list(set(fresh_ranges))
print(len(fresh_ranges))
fresh_ids = set()
fresh_ids.add(fresh_ranges[0])

temp_i = 0
for i in fresh_ranges[1:]:
    lb_, ub_ = i.split("-")
    lb_ = int(lb_)
    ub_ = int(ub_)
    temp_ids = list(fresh_ids).copy()
    temp_j = 0
    for j in temp_ids:
        lb, ub = j.split("-")
        lb = int(lb)
        ub = int(ub)
        if lb <= lb_ and ub >= ub_:
            continue
        if lb_ < lb and (ub_ >= lb and ub_ < ub):
            lb = lb_
        if (lb_ > lb and lb_ < ub) and ub_ > ub:
            ub = ub_
        if ub_ < lb or lb_ > ub:
            fresh_ids.add(i)
        temp_j +=1
    temp_i += 1

fresh_ids = list(fresh_ids)
final_count = 0
for i in fresh_ids:
    lb, ub = i.split("-")
    lb = int(lb)
    ub = int(ub)
    final_count += (ub - lb + 1)

print(final_count)

