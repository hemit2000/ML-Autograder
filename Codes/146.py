def countVowels(string):
    vowels = 'aeiouAEIOU'
    count = 0

    for char in string:
        if char in vowels:
            count += 1
    
    return count

string = "hello world"
vowel_count = countVowels(string)
print(vowel_count)
