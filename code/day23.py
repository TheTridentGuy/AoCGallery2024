import functools
import itertools
import collections
from pprint import pp, pprint
import re
with open("in.txt", "r") as f:
    i = f.read()
si = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""
import networkx
# Part 1:
def p1(i):
    """Part 1"""
    i = i.strip()
    i = [line.split("-") for line in i.split("\n")]
    lan = networkx.Graph()
    lan.add_edges_from(i)
    char = "t"
    l = []
    inter = [clique for clique in networkx.enumerate_all_cliques(lan) if len(clique)==3]
    pp(inter)
    for group in inter:
        for item in group:
            if item.startswith("t"):
                l.append(group)
                break
    return len(l)


print("Sample Input:", p1(p1si := si))
print(p1i := p1(i))
def p2(i):
    """Part 2"""
    i = i.strip()
    i = [line.split("-") for line in i.split("\n")]
    lan = networkx.Graph()
    lan.add_edges_from(i)
    char = "t"
    l = []
    inter = networkx.enumerate_all_cliques(lan)
    return ",".join(sorted(max(inter, key=lambda x: len(x))))


print("Part 2 - Sample Input:", p2si := p2(si))
print("", p2i := p2(i))
