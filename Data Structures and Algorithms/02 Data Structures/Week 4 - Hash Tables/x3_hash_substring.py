# python3

def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def polyhash(string, bucket_count=100000, multiplier=263, prime=1_000_000_007):
    ans = 0
    for c in reversed(string):
        ans = (ans * multiplier + ord(c)) % prime
    return ans % bucket_count


def get_occurrences_rk_fast(pattern, text):
    # Good job! (Max time used: 0.49/4.50, max memory used: 61808640/536870912.)
    mult = 263
    prime = 1_000_000_007
    # bucket_count = 100000
    bucket_count = prime

    if len(pattern) > len(text):
        return []
    h_pattern = polyhash(pattern, bucket_count, mult, prime)
    hits = []

    precomp_hashes = [0 for _ in range(len(text) - len(pattern) + 1)]
    last_hash = polyhash(text[-len(pattern):], bucket_count, mult, prime)
    precomp_hashes[-1] = last_hash

    highest_power = 1
    for i in range(1, len(pattern)+1):
        highest_power = (highest_power * mult) % prime

    for i in reversed(range(len(text) - len(pattern))):
        precomp_hashes[i] = (
                ord(text[i])  # the new starting char (we're walking backwards)
                + precomp_hashes[i+1] * mult  # the previous hash, now times x
                - ord(text[i+len(pattern)]) * highest_power  # remove the last char's contribution from the previous hash
        ) % prime

    for i in range(len(text) - len(pattern) + 1):
        if h_pattern == precomp_hashes[i]:
            if pattern == text[i:(i+len(pattern))]:
                hits.append(i)

    return hits


def get_occurrences_rk_slow(pattern, text):
    # Failed case #26/52: time limit exceeded (Time used: 8.98/4.50, memory used: 20369408/536870912.)
    if len(pattern) > len(text):
        return []

    h_pattern = polyhash(pattern)
    hits = []

    for i in range(len(text) - len(pattern) + 1):
        substr = text[i:(i+len(pattern))]
        h_substr = polyhash(substr)

        if h_pattern == h_substr:
            if pattern == substr:
                hits.append(i)

    return hits


def get_occurrences_naive(pattern, text):
    # The naive solution actually already passes the grader:
    # Good job! (Max time used: 2.37 / 4.50, max memory used: 62586880 / 536870912.)
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]


if __name__ == '__main__':
    print_occurrences(get_occurrences_rk_fast(*read_input()))

