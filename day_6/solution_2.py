import math

with open("day_6/input.txt", "r") as f:
    content = f.readlines()

content = [line.strip('\n') for line in content]


for i in range(len(content)):
    content[i] = content[i][::-1]

operands = content[-1].split(" ")
operands = [i for i in operands if i != ""]


result = []
operand_idx = 0
_temp_list = []
for i in range(len(content[0])):
        _test = True
        if _test == True:
            digit_0 = content[0][i].strip(" ")
            digit_1 = content[1][i].strip(" ")
            digit_2 = content[2][i].strip(" ")
            digit_3 = content[3][i].strip(" ")
            num = digit_0 + digit_1 + digit_2 + digit_3
            if num == "":
                if operands[operand_idx] == "+":
                    result.append(sum(_temp_list))
                else:
                    result.append(math.prod(_temp_list))
                operand_idx += 1
                _temp_list = []
                _test = False
            else:
                 _temp_list.append(int(num))

if operands[-1 ] == "+":
    result.append(sum(_temp_list))
else:
    result.append(math.prod(_temp_list))
print(result)
print(f"Final answer is {sum(result)}")
print("9876636978528")