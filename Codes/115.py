def binary_to_string(b_string):
 s = ""
 for i in range(0, len(b_string), 8):
    byte = b_string[i: i + 8]
 s += chr(int(byte, 2))
 return s

b_string = "0100100001100101011011000110110001101111"
print(binary_to_string(b_string))
