import json
json_data = '{"name": "Elizabete Maike", "age": 30, "city": "New York"}'
data  = json.loads(json_data)
# print(data)
# print(type(data))
# print(f"name: {data['name']}")
# print(f"age:{data['age']}")


def read_json_file(filename):
    """
    To read the json file
    :param filename:
    :return:
    """
    try:
        with open(filename, mode='r') as json_file:
            data = json.load(json_file)
            print(data['glossary']['GlossDiv']['GlossList']['GlossEntry']['Abbrev'])
            return data
    except Exception as ex:
        raise ex

print(read_json_file('data.json'))

##json.dump() --> for dump into file
## json.dumps() --> for dump into the object

def dump_json(filename, data):
    with open(filename, mode='w+') as json_file:
        json.dump(data, json_file)
        print(data)
    json_data = json.dumps(data, indent=4)
    print(json_data)

data = {'name': 'shrikant', 'place':'pune'}
dump_json('user.json', data)
