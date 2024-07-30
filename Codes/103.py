number_list = [2, 3, 5, 7, 11, 13, 17]
total = 0

for number in number_list:
    if number % 2 == 0:
        total += number

print(total)
