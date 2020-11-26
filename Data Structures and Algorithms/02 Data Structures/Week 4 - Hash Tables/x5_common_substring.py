# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')


def solve_slow(s, t):
	ans = Answer(0, 0, 0)
	for i in range(len(s)):
		for j in range(len(t)):
			for l in range(min(len(s) - i, len(t) - j) + 1):
				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
					ans = Answer(i, j, l)
	return ans


def get_substr_hashes(s, length):
	# TODO
	pass


def solve(s, t):
	max_k = min(len(s), len(t))
	min_k = 0

	while min_k != max_k:
		k_candidate = (min_k + max_k) // 2
		s_substr_hashes = get_substr_hashes(s, k)
		t_substr_hashes = get_substr_hashes(t, k)
		if s.substr_hashes.intersection(t_substr_hashes):
			# TODO
			pass


if __name__=='__main__':
	for line in sys.stdin.readlines():
		s, t = line.split()
		ans = solve(s, t)
		print(ans.i, ans.j, ans.len)
