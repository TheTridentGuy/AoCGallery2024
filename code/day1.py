with open("in.txt", "r") as f:
    lines = f.read().split("\n")
    l1 = []
    l2 = []
for line in lines:
    line = line.split(" ")
    l1.append(line[0])
    l2.append(line[3])
l1.sort()
l2.sort()
sum = 0
for i1, i2 in zip(l1,l2):
    sum+=abs(int(i1)-int(i2))
print(sum)
sum = 0
for i1 in l1:
    for i2 in l2:
        if i1==i2:
            sum+=int(i1)
print(sum)