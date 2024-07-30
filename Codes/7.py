def roman(number):
    roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
                      100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
                      10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    result = ''

    for num in roman_numerals.keys():
        while number >= num:
            result += roman_numerals[num]
            number -= num

    print(result)

number = int(input('Enter a number: '))
roman(number)
