import functools
import itertools
import collections
import math
import re
with open("in.txt", "r") as f:
    i = f.read()
si = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

# Part 1:
def p1(i):
    """Part 1"""
    machines = i.split("\n\n")
    for index, machine in enumerate(machines):
        machines[index] = machine.split("\n")
        machines[index][0] = re.findall(r"\d+", machines[index][0])
        machines[index][1] = re.findall(r"\d+", machines[index][1])
        machines[index][2] = re.findall(r"\d+", machines[index][2])
    print(machines)
    def solve_machine(machine):
        orig_best = 10000000000000
        best = 10000000000000
        ax = int(machine[0][0])
        ay = int(machine[0][1])
        bx = int(machine[1][0])
        by = int(machine[1][1])
        px = int(machine[2][0])
        py = int(machine[2][1])
        for b_pushes in range(100):
            x_travel = bx*b_pushes
            y_travel = by*b_pushes
            x_remaining = px-x_travel
            y_remaining = py-y_travel
            if x_remaining<0 or y_remaining<0:
                continue
            if x_remaining%ax==0 and y_remaining%ay==0 and x_remaining//ax == y_remaining//ay:
                a_pushes = x_remaining//ax
                if (a_pushes*3)+(b_pushes) < best:
                    best = (a_pushes*3)+(b_pushes)
        if best == orig_best:
            best = 0
        return best
    sum = 0
    for machine in machines:
        sum+=solve_machine(machine)
    return sum


print("Sample Input:", p1(p1si := si))
print(p1i := p1(i))
def p2(i):
    """Part 2"""
    machines = i.split("\n\n")
    for index, machine in enumerate(machines):
        machines[index] = machine.split("\n")
        machines[index][0] = re.findall(r"\d+", machines[index][0])
        machines[index][1] = re.findall(r"\d+", machines[index][1])
        machines[index][2] = re.findall(r"\d+", machines[index][2])
    print(machines)
    def solve_machine(machine):
        extra = 10000000000000
        ax = int(machine[0][0])
        ay = int(machine[0][1])
        bx = int(machine[1][0])
        by = int(machine[1][1])
        px = extra+int(machine[2][0])
        py = extra+int(machine[2][1])
        b_pushes = (ay * px - ax * py) / (ay * bx - ax * by)
        a_pushes = (px - bx * b_pushes) / ax
        if not b_pushes == int(b_pushes) or not a_pushes == int(a_pushes):
            return 0
        return (3*a_pushes)+b_pushes
    sum = 0
    i = 0
    l = len(machines)
    for machine in machines:
        sum+=solve_machine(machine)
        print(f"machine {i} of {l} done: {sum}")
        i+=1
    return int(sum)


print("Part 2 - Sample Input:", p2si := p2(si))
print("", p2i := p2(i))
