import heapq
from collections import deque
i = """###############
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

goal = goal[::-1]
start = start[::-1]
path = dijkstra_grid(imap, '#', start, goal)[1]

tmap = imap.copy()
print(path)
for y, x in path:
    tmap[y][x] = 'X'
for row in tmap:
    print(''.join(row))