def display_dict(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: {value}')

print(display_dict({'name': 'John', 'age': 25, 'city': 'New York'}))