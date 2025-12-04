# Load input data from file
with open('input.txt', 'r') as f:
    content = f.readlines()

joltage = []

for a in range(len(content)):
    content[a] = content[a].strip()

bank_joltage = []
for _ in content:
    joltage = _[:12]
    balance = _[12:]

    for i in balance:
        temp_joltage = joltage + i
        for j in range(len(temp_joltage) - 1):
            if int(temp_joltage[j]) < int(temp_joltage[j+1]):
                joltage = temp_joltage[:j] + temp_joltage[j+1:]
                break
    bank_joltage.append(int(joltage))
    
result = sum(bank_joltage)
print(f"Final result is {result}")

