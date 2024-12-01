# AOC Python Cheatsheet
## Imports
```python
import itertools
import collections
import heapq
import math
import functools
import operator
import re
```
## Input Parsing
```python
# Read all input as a string
raw_input = input()
# Read lines of input
lines = raw_input.splitlines()
# Split a line into integers
nums = list(map(int, line.split()))
# Split by custom delimiter
data = raw_input.split(',')
```
## Itertools
```python
# Cartesian product
itertools.product(A, B)  # Equivalent to nested for-loops
# Permutations
itertools.permutations(iterable, r=None)
# Combinations
itertools.combinations(iterable, r)
# Infinite iterators
itertools.count(start=0, step=1)
itertools.cycle(iterable)
itertools.repeat(object, times=None)
# Group by (requires sorted input for meaningful grouping)
for key, group in itertools.groupby(data):
    print(key, list(group))
```
## Collections
```python
# Counter
counter = collections.Counter(iterable)
most_common = counter.most_common(3)  # Top 3 elements
# defaultdict (with default factory)
def_dict = collections.defaultdict(list)
def_dict[key].append(value)
# deque (double-ended queue)
deque = collections.deque(maxlen=10)
deque.append(item)
deque.appendleft(item)
deque.pop()
deque.popleft()
# Named tuple
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
```
## Heapq (Priority Queue)
```python
# Min-heap
heap = []
heapq.heappush(heap, item)
heapq.heappop(heap)
heapq.heappushpop(heap, item)
heapq.heapify(data)
# Max-heap (invert values)
max_heap = []
heapq.heappush(max_heap, -item)
heapq.heappop(max_heap)
```
## Math
```python
math.gcd(a, b)  # Greatest common divisor
math.lcm(a, b)  # Least common multiple (Python 3.9+)
math.isqrt(n)   # Integer square root
math.comb(n, k) # Combinations (n choose k)
math.factorial(n)
math.prod(iterable)  # Product of iterable (Python 3.8+)
# Trigonometric and exponential
math.sin(x)
math.exp(x)
```
## String Manipulation
```python
# Pattern matching with regex
pattern = r"\d+"
re.findall(pattern, text)
re.sub(pattern, replacement, text)
# String slicing and reversing
reversed_string = s[::-1]
# String alignment
s.rjust(width)
s.ljust(width)
s.center(width)
```
## Functional Programming
```python
# Reduce (accumulate values)
result = functools.reduce(operator.add, iterable)
# Map
mapped = list(map(function, iterable))
# Filter
filtered = list(filter(function, iterable))
# Sorted with custom key
sorted_data = sorted(data, key=lambda x: x[1])
```
## Grid Utilities
```python
# Create a grid
grid = [[0] * cols for _ in range(rows)]
# Directions (4-way and 8-way)
dirs_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dirs_8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
# Iterate through a grid
for r in range(rows):
    for c in range(cols):
        value = grid[r][c]
# Check in-bounds
if 0 <= r < rows and 0 <= c < cols:
    pass
```
## Binary and Bitwise Operations
```python
# Convert to binary
bin_str = bin(number)[2:]  # Remove '0b' prefix
# Bitwise AND, OR, XOR, NOT
result = a & b
result = a | b
result = a ^ b
result = ~a
# Shift operators
result = a << 1  # Left shift
result = a >> 1  # Right shift
# Count set bits
bin(number).count('1')
```
## Debugging
```python
# Print with debug info
print(f"Variable name: {var}")
# Pretty print data structures
from pprint import pprint
pprint(data)
```