# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.hash_table = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == 'check':
            print(" ".join(reversed(self.hash_table[query.ind])))
        elif query.type == 'find':
            bucket = self._hash_func(query.s)
            print('yes' if query.s in self.hash_table[bucket] else 'no')
        elif query.type == 'add':
            # Don't add to the beginning of the chain (as per problem statement).
            # Instead, print list in reverse if query.type == 'check'
            bucket = self._hash_func(query.s)
            if query.s not in self.hash_table[bucket]:
                self.hash_table[bucket].append(query.s)
        elif query.type == 'del':
            bucket = self._hash_func(query.s)
            if query.s in self.hash_table[bucket]:
                self.hash_table[bucket].remove(query.s)
        else:
            raise ValueError('Unknown command')


class QueryProcessorNaive:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


def main():
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()


if __name__ == '__main__':
    main()
