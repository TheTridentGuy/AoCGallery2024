import functools
import itertools
import collections
from collections import deque
from copy import deepcopy
from pprint import pp, pprint
import re
import heapq

with open("in.txt", "r") as f:
    i = f.read()
si = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

# Part 1:
def p1(i):
    """Part 1"""
    size = 70
    bytes = 1024
    imap = [["."]*(size+1) for _ in range(size+1)]
    points = [line.split(",") for line in i.split("\n")]
    print(points)
    i = 0
    for x, y in points:
        if i >= bytes:
            break
        x, y = int(x), int(y)
        imap[y][x] = "#"
        i+=1
    for row in imap:
        print("".join(row))
    def bfs(grid, start, goal):
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        queue = deque([start])
        visited = set()
        visited.add(start)
        came_from = {}

        while queue:
            current = queue.popleft()
            # If we reached the goal, reconstruct the path
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]  # Reverse the path

            # Explore neighbors
            for dx, dy in directions:
                neighbor = (current[0] + dx, current[1] + dy)
                if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and
                        grid[neighbor[0]][neighbor[1]] == '.' and neighbor not in visited):
                    queue.append(neighbor)
                    visited.add(neighbor)
                    came_from[neighbor] = current

        return None  # No path found

    path = bfs(imap, (0,0), (size, size))
    print(path)
    return len(path)


#print("Sample Input:", p1(p1si := si))
print(p1i := p1(i))
def p2(i):
    """Part 2"""
    size = 70
    imap = [["."]*(size+1) for _ in range(size+1)]
    points = [line.split(",") for line in i.split("\n")]
    def bfs(grid, start, goal):
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        queue = deque([start])
        visited = set()
        visited.add(start)
        came_from = {}

        while queue:
            current = queue.popleft()
            # If we reached the goal, reconstruct the path
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]  # Reverse the path

            # Explore neighbors
            for dx, dy in directions:
                neighbor = (current[0] + dx, current[1] + dy)
                if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and
                        grid[neighbor[0]][neighbor[1]] == '.' and neighbor not in visited):
                    queue.append(neighbor)
                    visited.add(neighbor)
                    came_from[neighbor] = current

        return None  # No path found
    points.reverse()
    while bfs(imap, (0, 0), (size, size)):
        x, y = points.pop()
        x, y = int(x), int(y)
        imap[y][x] = "#"
    return f"{x},{y}"


#print("Part 2 - Sample Input:", p2si := p2(si))
print("", p2i := p2(i))
