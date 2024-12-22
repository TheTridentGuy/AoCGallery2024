import functools
import itertools
import collections
from pprint import pp, pprint
import re
import networkx as nx
with open("in.txt", "r") as f:
    i = f.read()
si = """029A
980A
179A
456A
379A"""

# Part 1:
def p1(i):
    """Part 1"""
    codes = i.split("\n")

    def optimize_path(path):
        path = path.split("A")
        optimized_path = []
        weights_odd = {
            "^": 0,
            "v": 1,
            "<": 2,
            ">": 3,
        }
        weights_even = {
            "^": 3,
            "v": 2,
            "<": 1,
            ">": 0,
        }
        for index, route in enumerate(path):
            if index % 2 == 0:
                route = sorted(route, key=lambda x: weights_even[x])
                optimized_path.append("".join(route))
            else:
                route = sorted(route, key=lambda x: weights_odd[x])
                optimized_path.append("".join(route))
        return "A".join(optimized_path)


    def solve_main_keypad(code):
        keypad_positions = {
            "7": (0, 0),
            "8": (1, 0),
            "9": (2, 0),
            "4": (0, 1),
            "5": (1, 1),
            "6": (2, 1),
            "1": (0, 2),
            "2": (1, 2),
            "3": (2, 2),
            "0": (1, 3),
            "A": (2, 3),
        }
        keypad = nx.Graph()
        for key1, pos1 in keypad_positions.items():
            keypad.add_node(key1, pos=pos1)
            for key2, pos2 in keypad_positions.items():
                if key1 != key2:
                    if abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) == 1:
                        keypad.add_edge(key1, key2)
        path = []
        last = "A"
        code = list(code)[::-1]
        while code:
            next = code.pop()
            if last is next:
                path.append("A")
            else:
                shortest = nx.shortest_path(keypad, source=last, target=next)
                for i in range(len(shortest) - 1):
                    current, next = shortest[i], shortest[i + 1]
                    if keypad_positions[next][0] > keypad_positions[current][0]:
                        path.append(">")
                    elif keypad_positions[next][0] < keypad_positions[current][0]:
                        path.append("<")
                    elif keypad_positions[next][1] > keypad_positions[current][1]:
                        path.append("v")
                    elif keypad_positions[next][1] < keypad_positions[current][1]:
                        path.append("^")
                last = next
                path.append("A")
        path = optimize_path("".join(path))
        print("mini:", path, len(path))
        return path


    def solve_mini_keypad(code):
        keypad_positions = {
            "^": (1,0),
            "A": (2, 0),
            "<": (0, 1),
            "v": (1, 1),
            ">": (2, 1),
        }
        keypad = nx.Graph()
        for key1, pos1 in keypad_positions.items():
            keypad.add_node(key1, pos=pos1)
            for key2, pos2 in keypad_positions.items():
                if key1 != key2:
                    if abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) == 1:
                        keypad.add_edge(key1, key2)
        path = []
        last = "A"
        code = list(code)[::-1]
        while code:
            next = code.pop()
            if last is next:
                path.append("A")
            else:
                shortest = nx.shortest_path(keypad, source=last, target=next)
                for i in range(len(shortest) - 1):
                    current, next = shortest[i], shortest[i + 1]
                    if keypad_positions[next][0] > keypad_positions[current][0]:
                        path.append(">")
                    elif keypad_positions[next][0] < keypad_positions[current][0]:
                        path.append("<")
                    elif keypad_positions[next][1] > keypad_positions[current][1]:
                        path.append("v")
                    elif keypad_positions[next][1] < keypad_positions[current][1]:
                        path.append("^")
                last = next
                path.append("A")
        path = optimize_path("".join(path))
        print("mini:", path, len(path))
        return path

    sum = 0
    for code in codes:
        sequence = solve_mini_keypad(solve_mini_keypad(solve_main_keypad(code)))
        print(f"{code}:", sequence)
        print(len(sequence), int(code[:-1]))
        sum += len(sequence) * int(code[:-1])
    return sum

print("Sample Input:", p1(p1si := si))
#print(p1i := p1(i))
def p2(i):
    """Part 2"""


print("Part 2 - Sample Input:", p2si := p2(si))
print("", p2i := p2(i))
