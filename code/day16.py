import functools
import itertools
import collections
from pprint import pp, pprint
import re
import heapq
with open("in.txt", "r") as f:
    i = f.read()
si = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""


def p1(i):
    """Part 1"""
    imap = [list(row) for row in i.split("\n")]
    sx = 1
    sy = len(imap)-2
    ex = len(imap[1])-2
    ey = 1
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def a_star(maze, start, end):
        
        pq = []
        
        costs = {}

        
        sx, sy = start
        ex, ey = end
        for i in range(4):
            heapq.heappush(pq, (0, sx, sy, i))  
            costs[(sx, sy, i)] = 0

        while pq:
            cost, x, y, direction = heapq.heappop(pq)

            
            if (x, y) == (ex, ey):
                return cost

            
            
            nx, ny = x + directions[direction][0], y + directions[direction][1]
            if maze[nx][ny] != '#':
                new_cost = cost + 1
                if (nx, ny, direction) not in costs or new_cost < costs[(nx, ny, direction)]:
                    costs[(nx, ny, direction)] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny, direction))

            
            for turn in [-1, 1]:  
                new_direction = (direction + turn) % 4
                if (x, y, new_direction) not in costs or cost + 1000 < costs[(x, y, new_direction)]:
                    costs[(x, y, new_direction)] = cost + 1000
                    heapq.heappush(pq, (cost + 1000, x, y, new_direction))

        return -1  
    return a_star(imap, (sx, sy), (ex, ey))

print("Sample Input:", p1(p1si := si))
print(p1i := p1(i))
def p2(i):
    """Part 2"""
    imap = [list(row) for row in i.split("\n")]
    sx = 1
    sy = len(imap)-2
    ex = len(imap[1])-2
    ey = 1
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def a_star(maze, start, end):
        pq = []
        costs = {}
        parent = {}
        sx, sy = start
        ex, ey = end
        for i in range(4):
            heapq.heappush(pq, (0, sx, sy, i))
            costs[(sx, sy, i)] = 0
        while pq:
            cost, x, y, direction = heapq.heappop(pq)
            if (x, y) == (ex, ey):
                path_cells = set()
                backtrack_all_paths(x, y, direction, parent, path_cells)
                path_cells.add(start)
                return len(path_cells)
            nx, ny = x + directions[direction][0], y + directions[direction][1]
            if maze[nx][ny] != '#':
                new_cost = cost + 1
                if (nx, ny, direction) not in costs or new_cost < costs[(nx, ny, direction)]:
                    costs[(nx, ny, direction)] = new_cost
                    parent[(nx, ny, direction)] = {(x, y, direction)}
                    heapq.heappush(pq, (new_cost, nx, ny, direction))
                elif new_cost == costs[(nx, ny, direction)]:
                    parent[(nx, ny, direction)].add((x, y, direction))
            for turn in [-1, 1]:
                new_direction = (direction + turn) % 4
                if (x, y, new_direction) not in costs or cost + 1000 < costs[(x, y, new_direction)]:
                    costs[(x, y, new_direction)] = cost + 1000
                    parent[(x, y, new_direction)] = {(x, y, direction)}
                    heapq.heappush(pq, (cost + 1000, x, y, new_direction))
                elif cost + 1000 == costs[(x, y, new_direction)]:
                    parent[(x, y, new_direction)].add((x, y, direction))
        return -1

    def backtrack_all_paths(x, y, direction, parent, path_cells):
        stack = [(x, y, direction)]
        while stack:
            cx, cy, cdir = stack.pop()
            if (cx, cy) not in path_cells:
                path_cells.add((cx, cy))
            for px, py, pdir in parent.get((cx, cy, cdir), []):
                stack.append((px, py, pdir))
    return a_star(imap, (sx, sy), (ex, ey))


print("Part 2 - Sample Input:", p2si := p2(si))
print("", p2i := p2(i))
