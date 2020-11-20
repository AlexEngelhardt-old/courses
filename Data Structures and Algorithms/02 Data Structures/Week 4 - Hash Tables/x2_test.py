from x2_hash_chains import QueryProcessor, QueryProcessorNaive, Query

buckets = 5
queries = [
    "add world",
    "add HellO",
    "check 4",
    "check 3",
    "find World",
    "find world",
    "del world",
    "check 4",
    "del HellO",
    "add luck",
    "add GooD",
    "check 2",
    "del good"
]

q1 = QueryProcessorNaive(buckets)
q2 = QueryProcessor(buckets)

for q in queries:
    q1.process_query(Query(q.split()))

print('*' * 40)

for q in queries:
    q2.process_query(Query(q.split()))