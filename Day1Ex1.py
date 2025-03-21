List1 = []
List2 = []

with open("Liste.txt", "r") as file:
    elements = file.read().split()

for i, num in enumerate(elements):
    if i % 2 == 0: 
        List1.append(int(num))
    else: 
        List2.append(int(num))

# Is it cheating ? Considering that .sort is way faster than a custom sort function
List1.sort()
List2.sort()

distance = sum(abs(a - b) for a, b in zip(List1, List2))

print("The total distance is :",distance)