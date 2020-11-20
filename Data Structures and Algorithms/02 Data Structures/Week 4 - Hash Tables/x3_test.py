from x3_hash_substring import get_occurrences_naive, get_occurrences_rk_slow, get_occurrences_rk_fast

P = "aba"
T = "abacaba"

print(f"find {P} in {T}")

print(get_occurrences_naive(P, T))
print(get_occurrences_rk_slow(P, T))
print(get_occurrences_rk_fast(P, T))