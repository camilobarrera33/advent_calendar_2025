with open('day_11/input.txt', 'r') as file:
    content = file.readlines()

content = [i.strip('\n') for i in content]
content = [i.split(' ') for i in content]

devices = {}
for i in content:
    devices[i[0][:-1]] = i[1:]


def find_out(_dict, start):
    print(f"checking path from {start}")
    count = 0
    if _dict[start] == ["out"]:
        print("Out found")
        return 1
    else:
        for i in _dict[start]:
            count += find_out(_dict, i)
        return count

paths = 0
paths += find_out(devices, "you")
print(f"Final number of paths: {paths}")