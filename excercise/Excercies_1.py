# Problem : Count API Request by end points
def count_api_request(api_list):
    api_dict = dict()
    for api in api_list:
        if api not in api_dict.keys():
            api_dict[api] = 1
        else:
            api_dict[api] += 1
    return api_dict

logs = [
    "/users",
    "/books",
    "/users",
    "/login",
    "/users",
    "/books"
]

# result = count_api_request(logs)
# print(result)


## Implement Pagination for an API
def paginate(data, page=1, size = 10):
    start = (page-1)*size
    end = start + 10
    result = data[start:end]
    return result

# data = [int(i) for i in range(1, 100)]
# result =  paginate(data, page=2, size=10)
# print(result)


##  decoder for function execution time

import time
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"{func.__name__}: {end-start:.4f} seconds")

        return result
    return wrapper

@measure_time
def process_data():
    time.sleep(1)
    return "process completed"

# print(process_data())


## Implement Retry Logic

def retry(max_attempts=3, delay =2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts+1):
                try:
                    func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempts: {attempt} failed")

                    if attempt == max_attempts:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def call_external_service():
    # API call
    print(10/0)

    return "success"

call_external_service()
