import heapq
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


class Worker:
    def __init__(self, i, free_at):
        self.i = i
        self.free_at = free_at

    # for heappush / _siftdown, we only need to implement the "<" operator:
    # https://github.com/python/cpython/blob/3.9/Lib/heapq.py
    def __lt__(self, other):
        if self.free_at == other.free_at:  # sort by two keys: If free_at is the same, take the dude with the lower ID
            return self.i < other.i
        return self.free_at < other.free_at


def assign_jobs_slow(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def assign_jobs(n_workers, jobs):
    heap = []
    for i in range(n_workers):
        w = Worker(i=i, free_at=0)
        heapq.heappush(heap, w)

    result = []
    for j in jobs:
        w = heapq.heappop(heap)
        result.append(AssignedJob(w.i, w.free_at))
        w.free_at += j
        heapq.heappush(heap, w)

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
