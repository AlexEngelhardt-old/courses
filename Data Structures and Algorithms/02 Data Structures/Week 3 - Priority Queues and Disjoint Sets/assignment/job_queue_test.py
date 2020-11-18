from job_queue import assign_jobs, assign_jobs_slow

n_workers = 2
jobs = [1, 2, 3, 4, 5]

res = assign_jobs_slow(n_workers, jobs)
for r in res:
    print(r.worker, r.started_at)

res = assign_jobs(n_workers, jobs)
for r in res:
    print(r.worker, r.started_at)
