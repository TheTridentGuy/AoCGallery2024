with open("in.txt", "r") as f:
    i = f.read()
si = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

# Part 1:
def p1(i):
    """Part 1"""
    imap = i.split("\n")
    imap = [list(item) for item in imap]
    for y in range(len(imap)):
        for x in range(len(imap[0])):
            imap[y][x] = int(imap[y][x])
    def get_next_pos(imap, x, y, visited):
        # if (x, y) in visited:
        #     return 0
        # visited.add((x, y))
        if imap[y][x] == 9:
            return 1
        directions = [(-1, 0), (1,0), (0, -1), (0, 1)]
        sum = 0
        print(visited)
        for dir in directions:
            if not (0 <= x + dir[0] and x+dir[0]<len(imap[0]) and 0 <= y + dir[1] < len(imap)):
                continue
            elif imap[y+dir[1]][x+dir[0]] == imap[y][x]+1:
                sum += get_next_pos(imap, x+dir[0], y+dir[1], visited)
        return sum
    fs = 0
    for y in range(len(imap)):
        for x in range(len(imap[0])):
            if imap[y][x] == 0:
                fs += get_next_pos(imap, x, y, set())
    return fs

print("Sample Input:", p1(si))
print(p1(i))
def p2(i):
    """Part 2"""


print(p2(i))
print("Sample Input:", p2(si))
