List1 = []
List2 = []

# Part2
tot = 0

with open("Liste.txt", "r") as file:
    elements = file.read().split()

for i, num in enumerate(elements):
    if i % 2 == 0: 
        List1.append(int(num))
    else: 
        List2.append(int(num))

# Sorting both lists
List1.sort()
List2.sort()

distance = sum(abs(a - b) for a, b in zip(List1, List2))
print(distance)

for i in List1:
    sum2 = 0
    for j in List2:
        if i == j:
            sum2 += 1

    tot += i * sum2

print(tot)
