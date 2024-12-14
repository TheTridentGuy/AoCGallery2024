import functools
import itertools
import collections
import re
with open("in.txt", "r") as f:
    i = f.read()
si = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

# Part 1:
def p1(i):
    """Part 1"""
    robots = i.split("\n")
    for index, robot in enumerate(robots):
        robots[index] = re.findall(r"-*\d+", robot)
    height = 103
    width = 101
    time = 100
    mp = [[[] for __ in range(width)] for _ in range(height)]
    print(robots)
    for index, robot in enumerate(robots):
        robot = tuple([int(s) for s in robot])
        print(robot)
        fullx = robot[0]+(time*robot[2])
        fully = robot[1]+(time*robot[3])
        finalx = fullx%(width)
        finaly = fully%(height)
        mp[finaly][finalx].append(robot)
    import pprint
    pprint.pp(mp)
    sectors = [0,0,0,0]
    for y in range(len(mp)):
        for x in range(len(mp[0])):
            if x<(len(mp[0])//2) and y<(len(mp)//2):
                sectors[0] += len(mp[y][x])
            elif x>len(mp[0])-(len(mp[0])//2)-1 and y<(len(mp)//2):
                sectors[1] += len(mp[y][x])
            elif x<(len(mp[0])//2) and y>len(mp)-(len(mp)//2)-1:
                sectors[2] += len(mp[y][x])
            elif x>len(mp[0])-(len(mp[0])//2)-1 and y>len(mp)-(len(mp)//2)-1:
                sectors[3] += len(mp[y][x])
    print(sectors)
    return sectors[0]*sectors[1]*sectors[2]*sectors[3]


#print("Sample Input:", p1(p1si := si))
print(p1i := p1(i))
def p2(i):
    """Part 2"""
    robots = i.split("\n")
    for index, robot in enumerate(robots):
        robots[index] = re.findall(r"-*\d+", robot)
    height = 103
    width = 101
    def map_after_t(time):
        mp = [[False for __ in range(width)] for _ in range(height)]
        for index, robot in enumerate(robots):
            robot = tuple([int(s) for s in robot])
            fullx = robot[0]+(time*robot[2])
            fully = robot[1]+(time*robot[3])
            finalx = fullx%(width)
            finaly = fully%(height)
            if mp[finaly][finalx]:
                return False
            mp[finaly][finalx] = True
        return True
    i = 0
    while True:
        if map_after_t(i):
            return i
        i+=1
        print(i)





print("Part 2 - Sample Input:", p2si := p2(si))
print("", p2i := p2(i))
