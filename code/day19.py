import functools
import itertools
import collections
from pprint import pp, pprint
import re
with open("in.txt", "r") as f:
    i = f.read()
si = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

# Part 1:
def p1(i):
    """Part 1"""
    i = i.split("\n\n")
    available = i[0].split(", ")
    patterns = i[1].split("\n")
    print(available, patterns)
    def can_do(pattern, available):
        pass

    def can_construct(s, words):
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string

        for i in range(1, n + 1):
            for word in words:
                if i >= len(word) and s[i - len(word):i] == word:
                    dp[i] = dp[i] or dp[i - len(word)]
        return dp[n]
    sum = 0
    for pattern in patterns:
        if can_construct(pattern, available):
            sum += 1
    return sum


print("Sample Input:", p1(p1si := si))
print(p1i := p1(i))
def p2(i):
    """Part 2"""
    i = i.split("\n\n")
    available = i[0].split(", ")
    patterns = i[1].split("\n")
    print(available, patterns)
    def can_do(pattern, available):
        pass

    def count_ways(s, wordDict):
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: there's one way to construct an empty string

        for i in range(1, n + 1):
            for word in wordDict:
                if i >= len(word) and s[i - len(word):i] == word:
                    dp[i] += dp[i - len(word)]  # Add the ways to construct the previous part

        return dp[n]
    sum = 0
    for pattern in patterns:
        sum += count_ways(pattern, available)
    return sum


print("Part 2 - Sample Input:", p2si := p2(si))
print("", p2i := p2(i))
