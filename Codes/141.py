def convert_string_to_number(str):
    try: 
        return int(str)
    except ValueError:
        try:
            return float(str)
        except ValueError:
            return "String could not be converted to number."

str = input("String: ")
print("Number:", convert_string_to_number(str))
