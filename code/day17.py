import functools
import itertools
import collections
from pprint import pp, pprint
import re
with open("in.txt", "r") as f:
    i = f.read()
si = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

# Part 1:
def p1(i):
    """Part 1"""
    i = i.split("\n\n")
    a, b, c = [int(n) for n in re.findall(r"\d+", i[0])]
    instructions = [int(n) for n in re.findall(r"\d+", i[1])]
    pointer = 0
    out = []
    def combo(operand):
        if 0<=operand<=3:
            return operand
        elif operand==4:
            return a
        elif operand==5:
            return b
        elif operand==6:
            return c
        elif operand==7:
            return None
        else:
            raise AssertionError("wtf", operand)
    while True:
        if pointer >= len(instructions):
            break
        opcode = instructions[pointer]
        operand = instructions[pointer+1]
        if opcode == 0:
            a = a//(2 ** combo(operand))
        elif opcode == 1:
            b = b^operand
        elif opcode == 2:
            b = combo(operand)%8
        elif opcode == 3:
            if a == 0:
                pass
            else:
                pointer = operand
                continue
        elif opcode == 4:
            b = b^c
        elif opcode == 5:
            out.append(combo(operand)%8)
        elif opcode == 6:
            b = a//(2 ** combo(operand))
        elif opcode == 7:
            c = a//(2 ** combo(operand))
        pointer += 2
    return ",".join([str(n) for n in out])

print("Sample Input:", p1(p1si := si))
print(p1i := p1(i))
def p2(i):
    """Part 2"""
    i = i.split("\n\n")
    a, b, c = [int(n) for n in re.findall(r"\d+", i[0])]
    instructions = [int(n) for n in re.findall(r"\d+", i[1])]
    def computer(a, b, c, instructions):
        pointer = 0
        out = []
        def combo(operand):
            if 0<=operand<=3:
                return operand
            elif operand==4:
                return a
            elif operand==5:
                return b
            elif operand==6:
                return c
            elif operand==7:
                return None
            else:
                raise AssertionError("wtf", operand)
        while True:
            if pointer >= len(instructions):
                break
            opcode = instructions[pointer]
            operand = instructions[pointer+1]
            if opcode == 0:
                a = a//(2 ** combo(operand))
            elif opcode == 1:
                b = b^operand
            elif opcode == 2:
                b = combo(operand)%8
            elif opcode == 3:
                if a == 0:
                    pass
                else:
                    pointer = operand
                    continue
            elif opcode == 4:
                b = b^c
            elif opcode == 5:
                out.append(combo(operand)%8)
            elif opcode == 6:
                b = a//(2 ** combo(operand))
            elif opcode == 7:
                c = a//(2 ** combo(operand))
            pointer += 2
        return out

    def compare_tail(a, b):
        n = 0
        for i in range(len(a)):
            if a[-(i + 1)] == b[-(i + 1)]:
                n += 1
            else:
                return n
    start = 216584204845050
    step = 1
    best = 10
    while True:
        for a in itertools.count(start, step=step):
            out = computer(a, b, c, instructions)
            if len(out) < len(instructions):
                start += step*10
                break
            if out == instructions:
                print(f"RESULT: {a} {instructions}=={out}")
                return None
            if not step <= 1 and compare_tail(out, instructions) > best:
                print(out, instructions)
                best = compare_tail(out, instructions)
                start = a - step
                step = step // 10
                print(start, step, best)
                break


#print("Part 2 - Sample Input:", p2si := p2(si))
print("", p2i := p2(i))
