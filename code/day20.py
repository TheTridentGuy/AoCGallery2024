import functools
import itertools
import collections
from copy import deepcopy
from pprint import pp, pprint
import re
from collections import deque
import heapq


with open("in.txt", "r") as f:
    i = f.read()
si = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

# Part 1:
def p1(i):
    """Part 1"""
    imap = [list(x) for x in i.split("\n")]
    for y in range(len(imap)):
        for x in range(len(imap[y])):
            if imap[y][x] == "S":
                start = (x, y)
            if imap[y][x] == "E":
                goal = (x, y)
    print(start, goal)
    for row in imap:
        print(''.join(row))

    def dijkstra_grid(grid, wall_val, start=(0, 0), end=None, save_distances=False):
        if not grid:
            return 0, []

        rows, cols = len(grid), len(grid[0])
        distances = {(r, c): float('inf') for r in range(rows) for c in range(cols)}
        distances[start] = 0

        min_heap = [(0, start)]
        path = {}

        while min_heap:
            dist, node = heapq.heappop(min_heap)
            r, c = node

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] != wall_val:
                    alt = dist + 1
                    if alt < distances[(new_r, new_c)]:
                        distances[(new_r, new_c)] = alt
                        heapq.heappush(min_heap, (alt, (new_r, new_c)))
                        path[(new_r, new_c)] = (r, c)

        if end not in path:
            return -1, []

        total_dist = distances[end]
        path_points = []
        current = end

        while current:
            path_points.append(current)
            current = path.get(current)

        path_points.reverse()
        return total_dist, path_points

    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    def get_cheats(path):
        cheats = []
        for index, p1 in enumerate(path):
            for p2 in path[index + 1:]:
                if manhattan_distance(p1, p2) <= 2 and (path.index(p2) - index) >= 102:
                    cheats.append((p1, p2))
        return cheats
    goal = goal[::-1]
    start = start[::-1]
    path = dijkstra_grid(imap, '#', start, goal)[1]
    print(path)
    tmap = deepcopy(imap)
    for row in tmap:
        print(''.join(row))
    for x, y in path:
        tmap[y][x] = 'X'
    for row in tmap:
        print(''.join(row))
    cheats = get_cheats(path)
    return len(cheats)


#print("Sample Input:", p1(p1si := si))
#print(p1i := p1(i))
def p2(i):
    """Part 2"""
    imap = [list(x) for x in i.split("\n")]
    for y in range(len(imap)):
        for x in range(len(imap[y])):
            if imap[y][x] == "S":
                start = (x, y)
            if imap[y][x] == "E":
                goal = (x, y)
    print(start, goal)
    for row in imap:
        print(''.join(row))

    def dijkstra_grid(grid, wall_val, start=(0, 0), end=None, save_distances=False):
        if not grid:
            return 0, []

        rows, cols = len(grid), len(grid[0])
        distances = {(r, c): float('inf') for r in range(rows) for c in range(cols)}
        distances[start] = 0

        min_heap = [(0, start)]
        path = {}

        while min_heap:
            dist, node = heapq.heappop(min_heap)
            r, c = node

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] != wall_val:
                    alt = dist + 1
                    if alt < distances[(new_r, new_c)]:
                        distances[(new_r, new_c)] = alt
                        heapq.heappush(min_heap, (alt, (new_r, new_c)))
                        path[(new_r, new_c)] = (r, c)

        if end not in path:
            return -1, []

        total_dist = distances[end]
        path_points = []
        current = end

        while current:
            path_points.append(current)
            current = path.get(current)

        path_points.reverse()
        return total_dist, path_points

    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    def get_cheats(path):
        cheats = []
        for index, p1 in enumerate(path):
            for p2 in path[index + 1:]:
                md = manhattan_distance(p1, p2)
                if md <= 20 and (path.index(p2) - index) >= 100+md:
                    cheats.append((p1, p2))
        return cheats
    goal = goal[::-1]
    start = start[::-1]
    path = dijkstra_grid(imap, '#', start, goal)[1]
    print(path)
    tmap = deepcopy(imap)
    for row in tmap:
        print(''.join(row))
    for x, y in path:
        tmap[y][x] = 'X'
    for row in tmap:
        print(''.join(row))
    cheats = get_cheats(path)
    return len(cheats)


print("Part 2 - Sample Input:", p2si := p2(si))
print("", p2i := p2(i))
