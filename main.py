

def count_vowels(input_string):

    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count


string = "Привет, как дела, my friend?"
result = count_vowels(string)
print(f"Количество гласных в строке: {result}")

