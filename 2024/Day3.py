import re

file = "Memory.txt"
with open(file, "r", encoding="utf-8") as f:
        content = f.read()

def sum_mul_in_file(files):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, files)
    total = sum(int(x) * int(y) for x, y in matches)  
    return total

total= sum_mul_in_file(content)
print("Part 1 :", total)

# Part 2

def Idontknowhowtocallit(content):
    while "don't" in content:
        try:
            start = content.index("don't")  
            end = content.index("do", start+3)  
            while content[end+2] == "n":
                end = content.index("do", end+3)  
            print("On va remove de",start,"à",end+len("do"))
            content = content[:start] + content[end + len("do"):]
        except ValueError:
            # If we are at the end and there's no do after don't like : don't ... don't ... [end_of_file]
            start = content.index("don't")
            content = content[:start]  
            break
    return content


new_content = Idontknowhowtocallit(content)
total2 = sum_mul_in_file(new_content)
print("Part 2 :", total2)
