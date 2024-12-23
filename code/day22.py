import functools
import itertools
import collections
from pprint import pp, pprint
import re
with open("in.txt", "r") as f:
    i = f.read()
si = """1
2
3
2024"""

# Part 1:
def p1(i):
    """Part 1"""
    i = [int(x) for x in i.split("\n")]
    def mix(a, b):
        return b^a
    def prune(a):
        return a % 16777216
    def get_x_secret_num(seed, loop_size):
        for _ in range(loop_size):
            seed = prune(mix(seed, seed*64))
            seed = prune(mix(seed, seed//32))
            seed = prune(mix(seed, seed*2048))
        return seed
    sum = 0
    for x in i:
        sum += get_x_secret_num(x, 2000)
    return sum

# print("Sample Input:", p1(p1si := si))
# print(p1i := p1(i))

def p2(i):
    """Part 2"""
    i = [int(x) for x in i.split("\n")]
    def mix(a, b):
        return b^a
    def prune(a):
        return a % 16777216
    sequences = {}
    def iter_seed(seed, loop_size):
        yield seed
        for _ in range(loop_size):
            seed = prune(mix(seed, seed*64))
            seed = prune(mix(seed, seed//32))
            seed = prune(mix(seed, seed*2048))
            yield seed
    def process_seed(seed, loop_size):
        sequence = []
        visited = set()
        nums = list(iter_seed(seed, loop_size))
        for i in range(1, 4):
            sequence.append((nums[i]%10)-(nums[i-1]%10))
        for i in range(4, loop_size+1):
            # print(sequence)
            sequence.append((nums[i]%10)-(nums[i-1]%10))
            sequence = ",".join([str(x) for x in sequence[-4:]])
            # print(sequence)
            # print(nums[i]%10)
            if sequence not in visited:
                seq_sell = sequences.get(sequence)
                sequences[sequence] = seq_sell+(nums[i]%10) if seq_sell else nums[i]%10
                visited.add(sequence)
            sequence = [int(x) for x in sequence.split(",")]
    for x in i:
        process_seed(x, 2000)
    return max(sequences.values())


print("Part 2 - Sample Input:", p2si := p2(si))
print("", p2i := p2(i))
