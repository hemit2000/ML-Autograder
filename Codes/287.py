def to_title_case(string):
    words = string.split()

    result = []
    for word in words:
        result.append(word.title())

    return ' '.join(result)

title = to_title_case("hello world")
print(title)
