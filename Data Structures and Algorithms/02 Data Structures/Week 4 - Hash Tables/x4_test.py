import cProfile
import pstats
from x4_substring_equality import SolverNaive, Solver

st = "trololo"
cases = [
    [0, 0, 7],
    [2, 4, 3],
    [3, 5, 1],
    [1, 3, 2]
]

sn = SolverNaive(st)
s = Solver(st)

for c in cases:
    print(sn.ask(*c))  # a, b, l

print('*' * 40)

for c in cases:
    print(s.ask(*c))  # a, b, l

print(s.substr_hashes)

print('*' * 40)

st = "abcdefghij" * 40000
s = Solver(st)
cProfile.run('[s.ask(100000, 200000, 10000) for _ in range(100)]')