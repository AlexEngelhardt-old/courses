import sys
import random


class SolverNaive:
	def __init__(self, s):
		self.s = s

	def ask(self, a, b, l):
		return self.s[a:a+l] == self.s[b:b+l]


class SolverTooSlow:
	"""Too slow because the initial substring polyhashing is O(len(s)**2). Make that smarter."""
	def __init__(self, s):
		self.s = s
		self.x = random.randint(0, 10**9)  # the integer for the polyhash
		self.n_buckets = 100000

		self.substr_hashes = [0] + [self.polyhash(s[:(i+1)]) for i in range(len(s))]

	def polyhash(self, s):
		res = 0
		for m, c in enumerate(reversed(s)):
			res += ord(c) * (self.x**m % self.n_buckets) % self.n_buckets
		return res % self.n_buckets

	def hash_substr(self, start, l):
		# hash of the length-l substring starting at char `start`
		h2 = self.substr_hashes[start+l] + self.n_buckets  # add that so that the minus works defo
		h1 = self.x**l * self.substr_hashes[start] % self.n_buckets
		return (h2 - h1) % self.n_buckets

	def ask(self, a, b, l):
		if self.hash_substr(a, l) == self.hash_substr(b, l):
			# return self.s[a:a+l] == self.s[b:b+l]  # takes too long. Just assume equality :3
			return True
		else:
			return False


class Solver:
	def __init__(self, s):
		self.s = s
		self.x = random.randint(1, 10 ** 9)  # the integer for the polyhash
		self.n_buckets = 10**9 + 7

		# TODO I should have used more than one hash function as per problem statement; e.g. one with buckets=10**9 + 9
		self.substr_hashes = [0 for _ in range(len(s)+1)]
		for i in range(1, len(self.s)+1):
			self.substr_hashes[i] = (self.substr_hashes[i-1]*self.x + ord(self.s[i-1])) % self.n_buckets

	def hash_substr(self, start, l):
		# hash of the length-l substring starting at char `start`
		h2 = self.substr_hashes[start + l] + self.n_buckets  # add that so that the minus works defo

		# pow(a, b, mod) computes a**b % mod efficiently
		# could precompute x**l in an array to save even more time tho:
		h1 = pow(self.x, l, self.n_buckets) * self.substr_hashes[start] % self.n_buckets
		return (h2 - h1) % self.n_buckets

	def ask(self, a, b, l):
		if self.hash_substr(a, l) == self.hash_substr(b, l):
			# return self.s[a:a+l] == self.s[b:b+l]  # takes too long. Just assume equality :3
			return True
		else:
			return False


if __name__ == '__main__':
	s = sys.stdin.readline()
	q = int(sys.stdin.readline())
	solver = Solver(s)
	for i in range(q):
		a, b, l = map(int, sys.stdin.readline().split())
		print("Yes" if solver.ask(a, b, l) else "No")
