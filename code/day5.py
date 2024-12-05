with open("in.txt", "r") as f:
    i = f.read()
si = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

# Part 1:
def p1(i):
    """Part 1"""
    def check_page(page, rules):
        for rule in rules:
            try:
                if not page.index(rule[0]) < page.index(rule[1]):
                    return False
            except ValueError:
                pass
        return True
    sum = 0
    i = i.split("\n\n")
    rules = i[0].split("\n")
    pages = i[1].split("\n")
    for i in range(len(rules)):
        rules[i] = rules[i].split("|")
    for page in pages:
        if check_page(page, rules):
            #print(page, rules)
            page = page.split(",")
            if not page[0]:
                continue
            #print(page, "middle: ", int(page[int(len(page)/2)]))
            sum += int(page[int(len(page)/2)])
    return sum


print(p1(i))
print("Sample Input:", p1(si))
def p2(i):
    """Part 2"""
    def check_page(page, rules):
        for rule in rules:
            try:
                if not page.index(rule[0]) < page.index(rule[1]):
                    return False
            except ValueError:
                pass
        return True
    def fix_page(page: str, rules):
        page = page.split(",")
        page2 = page.copy()
        for rule in rules:
            try:
                i1 = page.index(rule[0])
                i2 = page.index(rule[1])
                if i1 < i2:
                    continue
                page2[i1] = page[i2]
                page2[i2] = page[i1]
                page = page2.copy()
                #print(rule, i1, i2, page, page2)
            except ValueError:
                pass
        return page
    sum = 0
    i = i.split("\n\n")
    rules = i[0].split("\n")
    pages = i[1].split("\n")
    for i in range(len(rules)):
        rules[i] = rules[i].split("|")
    for page in pages:
        if check_page(page, rules):
            continue
        else:
            #print(page, end=" | ")
            page = ",".join(fix_page(page, rules))
            page = ",".join(fix_page(page, rules))
            page = ",".join(fix_page(page, rules))
            page = ",".join(fix_page(page, rules))
            page = ",".join(fix_page(page, rules))
            page = ",".join(fix_page(page, rules))
            page = ",".join(fix_page(page, rules))
            page = fix_page(page, rules)
            #print(page, sum, int(page[int(len(page)/2)]))
            sum += int(page[int(len(page)/2)])
    return sum



print(p2(i))
print("Sample Input:", p2(si))
