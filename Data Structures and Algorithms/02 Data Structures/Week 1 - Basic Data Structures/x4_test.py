from x4_stack_with_max_naive import StackWithMax, StackWithMaxNaive

queries = ["push 2", "push 1", "max", "pop", "max"]
# s1 = StackWithMaxNaive()
s1 = StackWithMax()

for query in queries:
    query = query.split()
    if query[0] == "push":
        s1.Push(int(query[1]))
    elif query[0] == "pop":
        s1.Pop()
    elif query[0] == "max":
        print(s1.Max())