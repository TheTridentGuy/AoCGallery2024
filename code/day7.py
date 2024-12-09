import itertools
from itertools import repeat

with open("in.txt", "r") as f:
    i = f.read()
si = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

# Part 1:
def p1(i):
    """Part 1"""
    lines = i.split("\n")
    sum = 0
    print(lines)
    for line in lines:
        if not line or not line[0]:
            continue
        line = line.split(":")
        num = int(line[0])
        line = line[1].split(" ")[1:]
        possible = itertools.product(list("*+"), repeat=len(line)-1)
        for combo in possible:
            line2 = line.copy()
            linesum = int(line2.pop(0))
            for op, char in zip(list(combo), list(line2)):
                if op == "+":
                    linesum += int(char)
                elif op == "*":
                    linesum *= int(char)
                else:
                   raise Exception("error", op, char)
            if linesum == num:
                print(linesum, num)
                print("- sum up")
                sum+=num
                break
    return sum


#print("Sample Input:", p1(si))
#print("Real input: ", p1(i))
def p2(i):
    """Part 2"""
    lines = i.split("\n")
    sum = 0
    print(lines)
    for line in lines:
        if not line or not line[0]:
            continue
        line = line.split(":")
        num = int(line[0])
        line = line[1].split(" ")[1:]
        possible = itertools.product(list("*+"), repeat=len(line)-1)
        cont = False
        for combo in possible:
            line2 = line.copy()
            linesum = int(line2.pop(0))
            for op, char in zip(list(combo), list(line2)):
                if op == "+":
                    linesum += int(char)
                elif op == "*":
                    linesum *= int(char)
                else:
                   raise Exception("error", op, char)
            if linesum == num:
                print(linesum, num)
                print("- sum up")
                sum+=num
                cont = True
                break
        if cont:
            continue
        possible = itertools.product(list("*+|"), repeat=len(line)-1)
        for combo in possible:
            line3 = line.copy()
            linesum = line3.pop(0)
            for op, char in zip(list(combo), list(line3)):
                if op == "|":
                    linesum = int(str(linesum)+char)
                    continue
                linesum = eval(str(linesum)+op+char)
            if linesum == num:
                print(linesum, num)
                print("- sum up")
                sum+=num
                break
    return sum


print("Sample Input:", p2(si))
print(p2(i))
