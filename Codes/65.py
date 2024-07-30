def sort_by_name(lst):
    return sorted(lst, key=lambda item: item["name"])

list_of_objects = [{"name": "John", "age": 35}, {"name": "Liz", "age": 25}, {"name": "Max", "age": 28}]
sorted_list = sort_by_name(list_of_objects)
print(sorted_list)
