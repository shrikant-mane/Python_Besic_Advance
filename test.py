import time




class TTLCache:
    def __init__(self):
        self.cache = {}

    def set(self, key, value, ttl):
        exp_time = time.time()+ ttl
        self.cache[key] = (value , exp_time)

    def get(self, key):
        if key not in self.cache:
            return -1

        value, exp_time = self.cache[key]
        if time.time() > exp_time:
            del self.cache[key]
            return -1
        return value

cache = TTLCache()
cache.set('user', 'shrikant', 10)
time.sleep(5)
print(cache.get('user'))