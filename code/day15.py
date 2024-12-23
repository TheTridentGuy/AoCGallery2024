import functools
import itertools
import collections
import sys
sys.setrecursionlimit(1500)
with open("in.txt", "r") as f:
    i = f.read()
si = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^"""


# Part 1:
def p1(i):
    """Part 1"""
    i = i.split("\n\n")
    imap = i[0].split("\n")
    moves = i[1]
    imap = [list(row) for row in imap]
    do_break = False
    for y in range(len(imap)):
        for x in range(len(imap[y])):
            if imap[y][x] == "@":
                bot_x = x
                bot_y = y
                do_break = True
                break
        if do_break:
            break
    directions = {
        "^": (0, -1),
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0),
    }

    def recursive_move(x, y, direction):
        if imap[y + direction[1]][x + direction[0]] == ".":
            imap[y + direction[1]][x + direction[0]] = imap[y][x]
            return True
        elif imap[y + direction[1]][x + direction[0]] == "O":
            if recursive_move(x + direction[0], y + direction[1], direction):
                imap[y + direction[1]][x + direction[0]] = imap[y][x]
                return True
            return False
        elif imap[y + direction[1]][x + direction[0]] == "#":
            return False
        else:
            raise AssertionError("what the fuck", x, y, direction, imap)

    for move in moves:
        if move == "\n":
            continue
        direction = directions[move]
        if recursive_move(bot_x, bot_y, direction):
            imap[bot_y][bot_x] = "."
            bot_x += direction[0]
            bot_y += direction[1]
    sum = 0
    for y in range(len(imap)):
        for x in range(len(imap[y])):
            if imap[y][x] == "O":
                sum += (100 * y) + x
    return sum


print("Sample Input:", p1(p1si := si))
print(p1i := p1(i))


def p2(i):
    """Part 2"""
    i = i.split("\n\n")
    imap = i[0].split("\n")
    moves = i[1]
    imap = [list(row) for row in imap]
    do_break = False
    nmap = [[] for _ in range(len(imap))]
    for y in range(len(imap)):
        for x in range(len(imap[y])):
            if imap[y][x] == "@":
                nmap[y].extend(["@", "."])
            elif imap[y][x] == "O":
                nmap[y].extend(["[", "]"])
            elif imap[y][x] == ".":
                nmap[y].extend([".", "."])
            elif imap[y][x] == "#":
                nmap[y].extend(["#", "#"])
    imap = nmap
    for y in range(len(imap)):
        for x in range(len(imap[y])):
            if imap[y][x] == "@":
                bot_x = x
                bot_y = y
                do_break = True
                break
        if do_break:
            break
    print(bot_x, bot_y)
    directions = {
        "^": (0, -1),
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0),
    }
    import pprint
    def r_x(x, y, dir, check=False):
        if imap[y][x+dir] == ".":
            if not check:
                imap[y][x+dir] = imap[y][x]
                imap[y][x] = "."
            return True
        elif imap[y][x+dir] == "]" or imap[y][x+dir] == "[":
            if r_x(x+dir, y, dir, True):
                if not check:
                    r_x(x+dir, y, dir)
                    imap[y][x+dir] = imap[y][x]
                    imap[y][x] = "."
                return True
            else:
                return False
        elif imap[y][x+dir] == "#":
            return False
        else:
            raise AssertionError("wtf")

    def r_y(x, y, dir, check=False):
        if imap[y+dir][x] == ".":
            if not check:
                imap[y + dir][x] = imap[y][x]
                imap[y][x] = "."
            return True
        elif imap[y+dir][x] == "]":
            if r_y(x-1, y+dir, dir, True) and r_y(x, y+dir, dir, True):
                if not check:
                    r_y(x-1, y+dir, dir)
                    r_y(x, y+dir, dir)
                    imap[y+dir][x] = imap[y][x]
                    imap[y][x] = "."
                return True
            else:
                return False
        elif imap[y+dir][x] == "[":
            if r_y(x+1, y+dir, dir, True) and r_y(x, y+dir, dir, True):
                if not check:
                    r_y(x+1, y+dir, dir)
                    r_y(x, y+dir, dir)
                    imap[y+dir][x] = imap[y][x]
                    imap[y][x] = "."
                return True
            else:
                return False
        elif imap[y+dir][x] == "#":
            return False
        else:
            raise AssertionError("wtf")


    for move in moves:
        if move == "\n":
            continue
        direction = directions[move]
        if direction[0] == 0:
            if r_y(bot_x, bot_y, direction[1]):
                imap[bot_y][bot_x] = "."
                bot_x += direction[0]
                bot_y += direction[1]
                imap[bot_y][bot_x] = "@"
        elif direction[1] == 0:
            if r_x(bot_x, bot_y, direction[0]):
                imap[bot_y][bot_x] = "."
                bot_x += direction[0]
                bot_y += direction[1]
                imap[bot_y][bot_x] = "@"

    sum = 0
    for y in range(len(imap)):
        for x in range(len(imap[y])):
            if imap[y][x] == "[":
                sum += (100 * y) + x
    return sum


print("Part 2 - Sample Input:", p2si := p2(si))
print("", p2i := p2(i))
