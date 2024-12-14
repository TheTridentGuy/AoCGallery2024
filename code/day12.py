import functools
import itertools
import collections
with open("in.txt", "r") as f:
    i = f.read()
si = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

# Part 1:
def p1(i):
    """Part 1"""
    imap = [list(it) for it in i.split("\n")]
    visited = set()
    def floodfill(x, y, imap):
        char = imap[y][x]
        area = 1
        perimeter = 0
        directions = [(-1, 0), (1,0), (0, -1), (0, 1)]
        if (x, y) in visited:
            return False, False
        visited.add((x,y))
        for dx, dy in directions:
            if not 0<=y+dy<len(imap) or not 0<=x+dx<len(imap[0]) or not imap[y+dy][x+dx] == char:
                perimeter += 1
            else:
                narea, nperimeter = floodfill(x+dx, y+dy, imap)
                area += narea
                perimeter += nperimeter
        return area, perimeter
    sum = 0
    for y in range(len(imap)):
        for x in range(len(imap[0])):
            area, perimeter = floodfill(x, y, imap)
            if area:
                sum+=(area*perimeter)
    return sum


print("Part 1 - Sample Input:", p1(p1si := si))
print(p1i := p1(i))
def p2(i):
    """Part 2"""
    imap = [list(it) for it in i.split("\n")]
    visited = set()
    def floodfill(x, y, imap):
        char = imap[y][x]
        area = 1
        perimeter = 0
        corners = 0
        directions = [(-1, 0), (1,0), (0, -1), (0, 1)]
        if (x, y) in visited:
            return False, False, False
        visited.add((x,y))
        for dx, dy in directions:
            if not 0<=y+dy<len(imap) or not 0<=x+dx<len(imap[0]) or not imap[y+dy][x+dx] == char:
                perimeter += 1
            else:
                ncorners, narea, nperimeter = floodfill(x+dx, y+dy, imap)
                area += narea
                perimeter += nperimeter
                corners += ncorners
        corner_coords = [
            ((-1, 0), (0, -1)),
            ((0, -1), (1, 0)),
            ((1, 0), (0, 1)),
            ((0, 1), (-1, 0))
        ]
        for corner in corner_coords:
            a = imap[y+corner[0][1]][x+corner[0][0]] if 0<=y+corner[0][1]<len(imap) and 0<=x+corner[0][0]<len(imap[0]) else "-"
            b = imap[y+corner[1][1]][x+corner[1][0]] if 0<=y+corner[1][1]<len(imap) and 0<=x+corner[1][0]<len(imap[0]) else "-"
            if not a == char and not b == char:
                corners += 1
        corner_coords = [
            ((-1, 0), (0, -1), (-1, -1)),
            ((0, -1), (1, 0), (1, -1)),
            ((1, 0), (0, 1), (1, 1)),
            ((0, 1), (-1, 0), (-1, 1))
        ]
        for corner in corner_coords:
            if 0<=y+corner[0][1]<len(imap) and 0<=x+corner[0][0]<len(imap[0]) and 0<=y+corner[1][1]<len(imap) and 0<=x+corner[1][0]<len(imap[0]) and 0<=y+corner[2][1]<len(imap) and 0<=x+corner[2][0]<len(imap[0]):
                if imap[y+corner[0][1]][x+corner[0][0]] == char and imap[y+corner[1][1]][x+corner[1][0]] == char and not imap[y+corner[2][1]][x+corner[2][0]] == char:
                    corners += 1
        return corners, area, perimeter
    sum = 0
    for y in range(len(imap)):
        for x in range(len(imap[0])):
            corners, area, perimeter = floodfill(x, y, imap)
            if area:
                sum+=(area*corners)
    return sum

print("Part 2 - Sample Input:", p2si := p2(si))
print(p2i := p2(i))
