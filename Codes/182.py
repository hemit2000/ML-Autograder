def make_float(string):
    try:
        return float(string)
    except ValueError:
        return None

string = "25.42"
result = make_float(string)
print(result)
