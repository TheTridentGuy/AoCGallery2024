with open("in.txt", "r") as f:
    i = f.read()
si = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMAS"""


# Part 1:
def p1(i):
    """Part 1"""
    sum = 0
    lines = i.split("\n")
    print(lines)
    def search(arr, x, y, string):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        rows, cols, count = len(arr), len(arr[0]), 0
        for dx, dy in directions:
            if all(0 <= x + i * dx < rows and 0 <= y + i * dy < cols and arr[x + i * dx][y + i * dy] == string[i] for i
                   in range(len(string))):
                count += 1
        return count
    for i in range(len(lines)):
        lines[i] = list(lines[i])
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            sum += search(lines, x, y, "XMAS")
    return sum



print(p1(i))
print("Sample Input:", p1(si))
def p2(i):
    """Part 2"""
    sum = 0
    lines = i.split("\n")
    print(lines)
    def search(arr, x, y, string):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        rows, cols, count = len(arr), len(arr[0]), 0
        for dx, dy in directions:
            if all(0 <= x + i * dx < rows and 0 <= y + i * dy < cols and arr[x + i * dx][y + i * dy] == string[i] for i
                   in range(len(string))):
                count += 1
        return count
    for i in range(len(lines)):
        lines[i] = list(lines[i])
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[x][y] == "A" and search(lines, x, y, "AS") > 1 and search(lines, x, y, "AM") > 1 and not lines[x+1][y-1] == lines[x-1][y+1]:
                sum += 1
    return sum


print(p2(i))
print("Sample Input:", p2(si))
