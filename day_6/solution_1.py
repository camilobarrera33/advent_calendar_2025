import math

# Read file
with open('day_6/input.txt', 'r') as f:
    content = f.readlines()

content = [line.strip('\n') for line in content]
for i in range(len(content)):
    content[i] = content[i].split(" ")
    content [i] = [j for j in content[i] if j != ""]

result = []
final_result = 0
for i in range(len(content[0])):
    numbers = []
    for j in range(len(content) - 1):
        numbers.append(int(content[j][i]))
    if content[-1][i] == "+":
        result.append(sum(numbers))
        final_result += sum(numbers)
    if content[-1][i] == "*":
        result.append(math.prod(numbers))
        final_result += math.prod(numbers) 

validation_result = sum(result)
print(f"Final answer is {final_result}")
print(f"Validation result is {validation_result}")