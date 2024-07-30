def celsius_to_fahrenheit(celsius):
    return ((celsius * 9/5 ) + 32)

temperature = 23
fahrenheit = celsius_to_fahrenheit(temperature)
print('The temperature in Fahrenheit is: ' + str(fahrenheit))
