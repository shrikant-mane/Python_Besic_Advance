import time

def find_duplicate_api(api_list):
    api_dict = dict()
    final_api_list = list()
    for api in api_list:
        if api not in api_dict.keys():
            api_dict[api] = 1
        else:
            api_dict[api] += 1

        # if api_dict[api] > 1:
        #     final_api_list.append(api)
    for k, v in api_dict.items():
        if v > 1:
            final_api_list.append(k)
    return final_api_list


requests = [
    ("user1", "/api/books", "GET"),
    ("user2", "/api/books", "GET"),
    ("user1", "/api/books", "GET"),
    ("user1", "/api/books/10", "GET"),
    ("user2", "/api/books", "GET"),
    ("user1", "/api/books", "GET"),
]

# result = find_duplicate_api(requests)
# print(result)



#### TTL cache
class TTLCache:

    def __init__(self):
        self.cache = {}

    def set(self, key, value, ttl):
        expiry_time = time.time() + ttl
        self.cache[key] = (value , expiry_time)

    def get(self, key):
        if key not in self.cache:
            return None

        value , expiry_time = self.cache[key]

        if time.time() > expiry_time:
            del self.cache[key]
            return None

        return value

    def delete(self, key):
        del self.cache[key, None]

# cache = TTLCache()
#
# # cache.set("username", "Shrikant", 10)
# # time.sleep(11)
# # print(cache.get("username"))


### LRU Cache
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        if key not in self.cache:
            return -1

        value = self.cache.pop(key)
        self.cache[key] = value
        print(self.cache)
        return value

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop()

        elif len(self.cache) >= self.capacity:
            self.cache.pop(next(iter(self.cache)))

        self.cache[key] = value


cache = LRUCache(3)
cache.put('name', 'shrikant')
cache.put('college', 'VIIT')
cache.put('stream', "Electronics and Telecommunications")

print(cache.get('stream'))
print(cache.get('name'))