file = "day4.txt"
with open(file, "r", encoding="utf-8") as f:
    content = f.read()

# Convert the content into a matrix
x = [[*map(str, line.split())] for line in content.split('\n') if line.strip()]
separated_matrix = [[char for char in row[0]] for row in x]

def check_around(x, y, matrix):
    directions = [(0, 1),(0, -1),(1, 0),(-1, 0),(1, 1),(1, -1),(-1, 1),(-1, -1)]
    howmany = 0

    for dx, dy in directions:
        check = []
        for i in range(4):
            new_x, new_y = x + i * dx, y + i * dy
            if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]):
                check.append(matrix[new_x][new_y])
            else:
                break

        if check == ['X', 'M', 'A', 'S']:
            howmany += 1

    return howmany


# Part 2
def check_aroundX_MAS(x, y, matrix):
    diag1 = [(-1, -1), (1, 1)]  # /
    diag2 = [(-1, 1), (1, -1)]  # \
    confirm = 0
    chars_diag1 = []
    for dx, dy in diag1:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]):
            chars_diag1.append(matrix[new_x][new_y])
        else:
            break 

    if set(chars_diag1) != {'M', 'S'}:
        pass
    else:
        confirm += 1

    chars_diag2 = []
    for dx, dy in diag2:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]):
            chars_diag2.append(matrix[new_x][new_y])
        else:
            break

    if set(chars_diag2) != {'M', 'S'}:
        pass
    else:
        confirm += 1
    if confirm == 2:
        return 1
    else:
        return 0



count = 0
#check XMAS
for row_idx, line in enumerate(separated_matrix):
    for col_idx, char in enumerate(line):
        if char == 'X':
            new_count = check_around(row_idx, col_idx, separated_matrix)
            if new_count > 0:
                count += new_count
                #print(count, row_idx, col_idx, new_count)  
print("Final Count:", count)

#check X-MAS
count = 0
for row_idx, line in enumerate(separated_matrix):
    for col_idx, char in enumerate(line):
        if char == 'A':
            new_count = check_aroundX_MAS(row_idx, col_idx, separated_matrix)
            if new_count > 0:
                count += new_count
                #print(count, row_idx, col_idx, new_count)
print("X-MAS Count:", count)