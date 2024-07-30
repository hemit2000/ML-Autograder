list = ["dog", "cat", "bird"]
target = "bird"

for element in list:
    if element == target:
        print("Target string found: {}".format(target))
        break
