import json

def array_obj_to_json(arr):
    json_arr = []
    for obj in arr:
        json_arr.append(json.dumps(obj))
    return json_arr

print(array_obj_to_json([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]))
