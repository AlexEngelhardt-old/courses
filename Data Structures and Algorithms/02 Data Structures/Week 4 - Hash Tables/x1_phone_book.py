# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    direct_address_book = [None] * (10**7 + 1)
    results = []

    for q in queries:
        if q.type == 'add':
            direct_address_book[q.number] = q.name
        elif q.type == 'del':
            direct_address_book[q.number] = None
        elif q.type == 'find':
            if q.number > (10**7 + 1):
                results.append('not found')
            elif direct_address_book[q.number]:
                results.append(direct_address_book[q.number])
            else:
                results.append('not found')
        else:
            raise ValueError('Unknown command')

    return results


def process_queries_slow(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else:  # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

