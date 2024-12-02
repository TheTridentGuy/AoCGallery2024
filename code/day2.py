with open("in.txt", "r") as f:
    i = f.read()
o = None
# Part 1:
o=0
for line in i.split("\n"):
    line = line.split(" ")
    line = [int(th) for th in line]
    b=list(line)
    line.sort()
    #print(b, l, l[::-1])
    if line==b or line[::-1]==b:
        bad = False
        for it in range(len(line) - 1):
            if abs(line[it] - line[it + 1])>3 or abs(line[it] - line[it + 1])<1:
                bad=True
                print(b, line, line[::-1])
                print("false")
        if not bad:
            print("true")
            o+=1

print(o)
print("part 2")
# Part 2:
o=0

def isbad(line2):
    b2=line2.copy()
    line2.sort()
    bad2 = True
    if line2==b2 or line2[::-1]==b2:
        bad2 = False
        for it2 in range(len(b2) - 1):
            if abs(b2[it2] - b2[it2 + 1]) > 3 or abs(b2[it2] - b2[it2 + 1]) < 1:
                bad2 = True
    return bad2

for line in i.split("\n"):
    line = line.split(" ")
    line = [int(th) for th in line]
    #print(b, l, l[::-1])
    print("working", line)
    if not isbad(line.copy()):
        o+=1
        continue
    bad = True
    for li in range(len(line)):
        lc = line.copy()
        lc.pop(li)
        print(line, lc)
        if not isbad(lc.copy()):
            print("this works")
            bad = False
            continue
    if not bad:
        o+=1
print(o)