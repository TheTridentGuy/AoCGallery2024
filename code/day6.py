with open("in.txt", "r") as f:
    i = f.read()
si = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

# Part 1:
def p1(i):
    """Part 1"""
    map1 = [list(line) for line in i.split("\n")]
    for y in range(len(map1)):
        for x in range(len(map1[y])):
            if map1[y][x] == "^":
                guardy = y
                guardx = x
                break
    def move(x,y,map3,dirx,diry):
        try:
            if x+dirx < 0 or x+dirx >= len(map3[0]):
                return False
            elif y+diry < 0 or y+diry >= len(map3):
                return False
            elif map3[y+diry][x+dirx] == "#":
                return "r"
            else:
                return "m"
        except:
            return False

    def trace(x, y, map2):
        actions = {
            "^": (0, -1),
            ">": (1, 0),
            "v": (0, 1),
            "<": (-1, 0),
        }
        lsact = ["^", ">", "v", "<"]
        lsact.reverse()
        action = move(x, y, map2, *actions[map2[y][x]])
        if not action:
            return False, None, None, map2
        elif action == "r":
            if map2[y][x] == "x":
                return "l", x, y, map2
            map2[y][x]=lsact[lsact.index(map2[y][x]) - 1]
            return True, x, y, map2
        else:
            act = map2[y][x]
            map2[y][x] = "x"
            y = y+actions[act][1]
            x = x+actions[act][0]
            map2[y][x] = act
            return True, x, y, map2

    while True:
        sum = 0
        status, guardx, guardy, map1 = trace(guardx, guardy, map1)
        if not status:
            for y in range(len(map1)):
                for x in range(len(map1[y])):
                    if map1[y][x] == "x":
                        sum+=1
            return sum+1

def p2(i):
    """Part 2"""
    map1 = [list(line) for line in i.split("\n")]
    def p1for2(map1):
        guardy1 = 0
        guardx1 = 0
        for y in range(len(map1)):
            for x in range(len(map1[y])):
                if map1[y][x] == "^":
                    guardy1 = y
                    guardx1 = x
                    break
        def move(x,y,map3,dirx,diry):
            try:
                if x+dirx < 0 or x+dirx >= len(map3[0]):
                    return False
                elif y+diry < 0 or y+diry >= len(map3):
                    return False
                elif map3[y+diry][x+dirx] == "#":
                    return "r"
                else:
                    return "m"
            except:
                return False

        def trace(x, y, map2):
            actions = {
                "^": (0, -1),
                ">": (1, 0),
                "v": (0, 1),
                "<": (-1, 0),
            }
            lsact = ["^", ">", "v", "<"]
            lsact.reverse()
            action = move(x, y, map2, *actions[map2[y][x]])
            lastr = False
            if not action:
                return False, None, None, map2
            elif action == "r":
                lastr = True
                map2[y][x]=lsact[lsact.index(map2[y][x]) - 1]
                return True, x, y, map2
            else:
                act = map2[y][x]
                map2[y][x] = "x"
                y = y+actions[act][1]
                x = x+actions[act][0]
                if lastr and map2[y][x] == "x":
                    return "l", None, None, map2
                map2[y][x] = act
                lastr = False
                return True, x, y, map2
        iters = 0
        while True:
            status, guardx1, guardy1, map1 = trace(guardx1, guardy1, map1)
            if status == "l" or iters > 17030:
                return "l"
            elif not status:
                return None
            iters += 1
    sum = 0
    import copy
    for y in range(len(map1)):
        for x in range(len(map1[y])):
            if map1[y][x] == ".":
                try:
                    print("working new map")
                    newmap = copy.deepcopy(map1)
                    newmap[y][x] = "#"
                    sum += 1 if p1for2(newmap) == "l" else 0
                except:
                    pass
    return sum



print(p1(i))
print("Sample Input:", p1(si))
print(p2(i))
print("Sample Input:", p2(si))
