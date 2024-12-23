import string
with open("in.txt", "r") as f:
    i = f.read()
si = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

# Part 1:
def p1(i):
    """Part 1"""
    antinodes = []
    lines = [list(sm) for sm in i.split("\n")]
    def find_all(item, lines):
        finds = []
        for y, line in enumerate(lines):
            for x, spot in enumerate(line):
                if spot == item:
                    finds.append((x,y))
        return finds
    def compute_an(x, y, lines):
        an = []
        for fx, fy in find_all(lines[y][x], lines):
            if fx == x and fy == y:
                continue
            ax = x-(fx-x)
            ay = y-(fy-y)
            an.append((ax, ay))
            ax = fx+(fx-x)
            ay = fy+(fy-y)
            an.append((ax, ay))
        return an

    allan = []
    for y, line in enumerate(lines):
        for x, spot in enumerate(line):
            if spot in (string.ascii_letters+string.digits):
                an = compute_an(x, y, lines)
                allan.extend(an)
    goodan = []
    #print(allan)
    for x, y in allan:
        if x < len(lines[0]) and x >= 0 and y < len(lines) and y >= 0:
            goodan.append((x, y))
            #print(x,y)
            lines[y][x] = "#"
    goodan = list(set(goodan))
    #print(goodan)
    import pprint
    #pprint.pprint(lines)
    return len(goodan)


print(p1(i))
print("Sample Input:", p1(si))
def p2(i):
    """Part 2"""
    """Part 1"""
    antinodes = []
    lines = [list(sm) for sm in i.split("\n")]

    def find_all(item, lines):
        finds = []
        for y, line in enumerate(lines):
            for x, spot in enumerate(line):
                if spot == item:
                    finds.append((x, y))
        return finds

    def compute_an(x, y, lines):
        an = []
        for fx, fy in find_all(lines[y][x], lines):
            if fx == x and fy == y:
                continue
            for i in range(60):
                ax = x - (i*(fx - x))
                ay = y - (i*(fy - y))
                an.append((ax, ay))
            for i in range(60):
                ax = fx + (i*(fx - x))
                ay = fy + (i*(fy - y))
                an.append((ax, ay))
        return an

    allan = []
    for y, line in enumerate(lines):
        for x, spot in enumerate(line):
            if spot in (string.ascii_letters + string.digits):
                an = compute_an(x, y, lines)
                allan.extend(an)
    goodan = []
    # print(allan)
    for x, y in allan:
        if x < len(lines[0]) and x >= 0 and y < len(lines) and y >= 0:
            goodan.append((x, y))
            # print(x,y)
            lines[y][x] = "#"
    goodan = list(set(goodan))
    # print(goodan)
    import pprint
    # pprint.pprint(lines)
    return len(goodan)

print(p2(i))
print("Sample Input:", p2(si))
