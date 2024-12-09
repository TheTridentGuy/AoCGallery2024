with open("in.txt", "r") as f:
    i = f.read()
si = """2333133121414131402"""

# Part 1:
def p1(i):
    """Part 1"""
    fs = []
    id = 0
    for index, digit in enumerate(i):
        digit = int(digit)
        if (index % 2) == 0:
            fs.extend([str(id) for _ in range(digit)])
            id +=1
        else:
            fs.extend(["." for _ in range(digit)])
    i = 0
    while i < len(fs):
        while fs[-1] == ".":
            fs.pop()
        if fs[i] == ".":
            fs[i] = fs.pop()
        i+=1
    sum = 0
    for index, item in enumerate(fs):
        if not item:
            continue
        sum += (index*int(item))
    return sum

print(p1(i))
print("Sample Input:", p1(si))

def p2(i):
    """Part 2"""
    fs = []
    id = 0
    def pp(fs):
        nfs = []
        for pair in fs:
            nfs.extend([pair[0]]*pair[1])
        return nfs
    for index, digit in enumerate(i):
        digit = int(digit)
        if (index % 2) == 0:
            fs.append([id, digit])
            id +=1
        elif digit > 0:
            fs.append([None, digit])
    def get_last_id(fs, cap):
        fs=fs.copy()
        while fs:
            item = fs.pop()
            if item[0] and int(item[0]) < cap:
                return len(fs), item
        return False, False
    last_file = [1000000]
    #print(pp(fs))
    while True:
        index = 0
        while index+1 < len(fs):
            if fs[index][0] is None and fs[index+1][0] is None:
                fs[index][1] += fs[index+1][1]
                fs.pop(index+1)
            else:
                index +=1
        lf_index, last_file = get_last_id(fs, last_file[0])
        if not last_file:
            break
        for index, part in enumerate(fs):
            if part[0] is None and index < lf_index:
                if part[1] > last_file[1]:
                    fs[lf_index] = [None, last_file[1]]
                    fs[index] = last_file
                    fs.insert(index+1, [None, part[1]-last_file[1]])
                    break
                elif part[1] == last_file[1]:
                    fs[lf_index] = [None, last_file[1]]
                    fs[index] = last_file
                    break
        #print(pp(fs))
    sum = 0
    nfs = pp(fs)
    for index, item in enumerate(nfs):
        if item:
            sum += index*int(item)
    return sum




print(p2(i))
print("Sample Input:", p2(si))
