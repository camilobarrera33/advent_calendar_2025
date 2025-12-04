# Load input data from file
with open('input.txt', 'r') as f:
    content = f.readlines()

joltage = []

# Clean up the input data by stripping whitespace characters
for a in range(len(content)):
    content[a] = content[a].strip()

# Iterate through each line in the content
for i in content:
    # Set initial values for finding the two largest digits
    first_idx = -1
    first_digit = 0
    second_idx = -1
    second_digit = 0
    # Iterate from first to second to last digit to find the largest digit
    for j in range(len(i) - 1):
        if int(i[j]) > first_digit:
            first_digit = int(i[j])
            first_idx = j
    # Iterate from the digit after the largest to the end to find the second largest digit
    for k in range(first_idx + 1, len(i)):
        if int(i[k]) > second_digit:
            second_digit = int(i[k])
            second_idx = k

    # Combine the two largest digits to form the bank joltage
    bank_joltage = int(str(first_digit) + str(second_digit))
    joltage.append(bank_joltage)

# Sum all the bank joltage values to get the final result
final_result = sum(joltage)
print(f"Final result is {final_result}")