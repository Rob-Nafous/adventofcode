file = "XMAS.txt"
with open(file, "r", encoding="utf-8") as f:
    content = f.read()

# Convert the content into a matrix
x = [[*map(str, line.split())] for line in content.split('\n') if line.strip()]
separated_matrix = [[char for char in row[0]] for row in x]

def check_around2(x, y, matrix):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
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

count = 0


for row_idx, line in enumerate(separated_matrix):
    for col_idx, char in enumerate(line):
        if char == 'X':
            new_count = check_around2(row_idx, col_idx, separated_matrix)
            if new_count > 0:
                count += new_count
                print(count, row_idx, col_idx, new_count)  

print("Final Count:", count)
