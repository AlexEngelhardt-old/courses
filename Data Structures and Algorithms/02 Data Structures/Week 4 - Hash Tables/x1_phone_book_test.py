from x1_phone_book import process_queries, Query

queries = [
    "find 3839442",  # not found
    "add 123456 me",
    "add 0 granny",
    "find 0",  # granny
    "find 123456",  # me
    "del 0",
    "del 0",
    "find 0"  # not found
]

queries = [Query(q.split()) for q in queries]

print(process_queries(queries))