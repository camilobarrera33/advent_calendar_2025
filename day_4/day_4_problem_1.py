# Read input file
with open('day_4/input.txt', 'r') as file:
    content = file.readlines()

# Remove linebreaks at the end of each line
content = [line.strip('\n') for line in content]

def get_indexes(idx, max_index, min_index=0):
    """Get the adjacent indexes for a given index"""
    if idx == max_index:
        return [idx - 1, idx]
    elif idx == min_index:
        return [idx, idx + 1]
    else:
        return [idx - 1, idx, idx + 1]
    
def get_neighbors(idx_1, idx_2, max_index_1, max_index_2, min_index):
    """Returns the adjacent neighbors of a set of indexes"""
    rows_ = get_indexes(idx_1, max_index_1, min_index)
    columns_ = get_indexes(idx_2, max_index_2, min_index)
    neighbors = [(i, j) for i in rows_ for j in columns_]
    neighbors.remove((idx_1, idx_2))
    return neighbors


access = []
max_rows = len(content) - 1
# Loop through each row
for t in range(len(content)):
    # Create temp variable for that row
    test = content[t]
    # Determine what is the max number of columns in that row
    max_cols = len(test) - 1
    # Loop through each column in that row
    for i in range(len(test)):
        # Check to only calculate for '@' symbols
        if content[t][i] == '@': 
            # Get the list of neighbor indexes
            idx_list = get_neighbors(t, i, max_rows, max_cols, 0)
            rolls = []
            # Loop through each neighbor index to determine if it is an '@' symbol
            for z in idx_list:
                r_ = z[0]
                c_ = z[1]
                # if it is an '@' symbol, append a roll of 1
                if content[r_][c_] == '@':
                    rolls.append(1)
            total_rolls = sum(rolls)
            # If there are less than 4 '@' neighbors, append 1 to access list
            if total_rolls < 4:
                access.append(1)

final_answer = sum(access)
print(f"Final Answer is {final_answer}")