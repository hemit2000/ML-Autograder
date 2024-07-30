def remove_punc_and_whitespace(string):
    punctuation = " ,;:-!?."
    return ''.join([x for x in string if x not in punctuation])

input_string = "Hello, how are you! I'm doing great."
output_string = remove_punc_and_whitespace(input_string)
print(output_string)
