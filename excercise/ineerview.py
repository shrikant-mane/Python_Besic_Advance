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

result = find_duplicate_api(requests)
print(result)



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

cache = TTLCache()

cache.set("username", "Shrikant", 10)
time.sleep(11)
print(cache.get("username"))


