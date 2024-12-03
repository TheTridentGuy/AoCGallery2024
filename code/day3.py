import re
from gc import enable

with open("in.txt", "r") as f:
    i = f.read()
si = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

# Part 1:
def p1(i):
    """Part 1"""
    def mul(x,y):
        return x*y
    finds = re.findall(pattern=r"mul\(\d+,\d+\)", string=i)
    sum = 0
    for f in finds:
        sum += eval(f)
    return sum

print(p1(i))
print("Sample Input:", p1(si))
def p2(i):
    """Part 2"""
    def mul(x,y):
        return x*y
    finds = re.findall(pattern=r"mul\(\d+,\d+\)|do\(\)|don't\(\)", string=i)
    sum = 0
    enabled = True
    for f in finds:
        if f == "do()":
            enabled = True
            continue
        elif f=="don't()":
            enabled = False
            continue
        if enabled:
            try:
                sum += eval(f)
            except:
                pass
    return sum


print(p2(i))
print("Sample Input:", p2(si))
