from x3_process_packages import Request, Response, Buffer, process_requests

buffer_size = 2
n_requests = 2
requests = [
    Request(arrived_at=0, time_to_process=1),
    Request(arrived_at=0, time_to_process=1)
]

buffer = Buffer(buffer_size)
responses = process_requests(requests, buffer)

for response in responses:
    print(response.started_at if not response.was_dropped else -1)
