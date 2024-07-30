def classify_list(input_list):
    result = {"low": [], "mid": [], "high": []}
    for num in input_list:
        if num < 4:
            result["low"].append(num)
        elif num < 10:
            result["mid"].append(num)
        else:
            result["high"].append(num)
    return result

input_list = [1, 2, 5, 9, 20]
result = classify_list(input_list)
print(result)
