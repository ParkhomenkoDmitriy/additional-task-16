
def get_valid_name():
    while True:
        name = input("Enter your name: ")
        # Убираем все пробелы
        if name.replace(" ", "").isalpha():
            return name  # Если условие выполнено, возвращаем имя
        else:
            print("The name must contain only letters and spaces.")

name = get_valid_name()

age = input('How old are you? ')
while not age.isdigit():
    print('age must contain only numbers.')
    age = input('Please enter your age again: ')

print(f'Hello, {name.title()}, you are {age} years old')

vowels = set("aeiouAEIOU")

# Счетчики
vowel_count = 0
consonant_count = 0

# счетчик гласных, согласный
for char in name.replace(' ', ''):
    if char in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print(f'number of consonants in your name: {consonant_count}')
print(f'number of vowels in your name: {vowel_count}')
