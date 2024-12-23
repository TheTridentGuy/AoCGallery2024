import functools


with open("in.txt", "r") as f:
    i = f.read()
si = """125 17"""

# Part 1:
def p1(i):
    """Part 1"""
    stones = i.split(" ")
    for _ in range(25):
        print(_, " ".join(stones))
        index = 0
        while index < len(stones):
            stone = stones[index]
            if int(stone) == 0:
                stones[index] = "1"
                index += 1
            elif len(stone) % 2 == 0:
                s1 = int(stone[:(len(stone)//2)])
                s2 = int(stone[(len(stone)//2):])
                print(s1,s2)
                stones[index] = str(s1)
                stones.insert(index+1, str(s2))
                index += 2
            else:
                stones[index] = str(int(stones[index])*2024)
                index += 1
    return len(stones)



#print("Sample Input:", p1(si))
#print(p1(i))
def p2(i):
    """Part 2"""
    stones = i.split(" ")
    sum = 0
    @functools.cache
    def go_deep(stone, depth):
        print(depth)
        if depth == 75:
            return 1
        sum = 0
        if int(stone) == 0:
            sum += (go_deep("1", depth+1))
        elif len(stone) % 2 == 0:
            s1 = int(stone[:(len(stone)//2)])
            s2 = int(stone[(len(stone)//2):])
            sum += go_deep(str(s1), depth+1)
            sum += go_deep(str(s2), depth+1)
        else:
            sum += go_deep(str(int(stone)*2024), depth+1)
        return sum
    for stone in stones:
        sum += go_deep(stone, 0)
    return sum





print("Sample Input:", p2(si))
print(p2(i))
