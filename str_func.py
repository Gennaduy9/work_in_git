"""
Функция которая принимает на вход строку и возвращает ее в верхнем регистре.
"""
def uppercase_string(input_string):
    return input_string.upper()

# Пример использования

string = "Hello, World!"
upper_string = uppercase_string(string)
print(upper_string) # выводит "HELLO, WORLD!"