import time

class RateLimiter:

    def __init__(self, max_requests, window):
        self.max_request = max_requests
        self.window = window
        self.request = dict()

    def allow(self, user_id):

        current_time = time.time()

        if user_id not in self.request:
            self.request[user_id] = []

        self.request[user_id] = [
            timestamp
            for timestamp in self.request[user_id]
            if current_time -timestamp < self.window
        ]

        # Check request limit
        if len(self.request[user_id]) >= self.max_request:
            return False

        self.request[user_id].append(current_time)
        print(self.request[user_id])
        return True

limiter = RateLimiter(max_requests=5, window=60)

print(limiter.allow('user_101'))
for i in range(7):
    print(f"Request {i + 1} -> {limiter.allow('user_101')}")


