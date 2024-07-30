def fahrenheit_to_celsius(temp_f):
    return (temp_f - 32) * 5 / 9

temp_f = float(input('Enter temperature in Fahrenheit:'))
temp_c = fahrenheit_to_celsius(temp_f)

print(f'{temp_f}F = {temp_c}C')
