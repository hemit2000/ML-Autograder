import itertools

def find_subsets(s):
    subsets = []

    for i in range(len(s)+1):
        for subset in itertools.combinations(s, i):
            subsets.append(subset)

    return subsets

s = {1, 2, 3}
result = find_subsets(s)
print(result)
