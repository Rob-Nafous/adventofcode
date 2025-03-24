safe_reports = 0

def Check(list):
    check_croissance=0
    check_decroissance=0
    chance = 0
    for i in range(0, len(list) - 1):
        if list[i] < list[i + 1]:
            check_croissance+=1
            if list[i] - list[i + 1] < -3:
                return False
        elif list[i] > list[i + 1]:
            check_decroissance+=1
            if list[i] - list[i + 1] > 3:
                return False
    if check_croissance+1==len(list) or check_decroissance+1==len(list):
        return True
    else:        
        return False

with open("Reports.txt", "r") as file:
    for line in file:
        numbers = line.strip().split() 
        numbers = [int(num) for num in numbers]
        if Check(numbers):
            safe_reports += 1
print(safe_reports)


# Part2

def Check_Dampener(row):
    for i in range(len(row)):  
        temp_row = row[:i] + row[i + 1:] 
        
        inc = [temp_row[j + 1] - temp_row[j] for j in range(len(temp_row) - 1)]
        if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
            return True 
    return False  


safe_reports = 0
with open("Reports.txt", "r") as file:
    for line in file:
        numbers = list(map(int, line.strip().split()))
        if Check_Dampener(numbers):
            safe_reports += 1

print("Dampener :", safe_reports)