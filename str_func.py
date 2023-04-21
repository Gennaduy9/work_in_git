"""
Функция которая принимает на вход строку и возвращает ее в верхнем регистре.
"""
def uppercase_string(input_string):
    return input_string.upper()

# Пример использования

string = "Hello, World!"
upper_string = uppercase_string(string)
print(f"{upper_string}\n") # выводит "HELLO, WORLD!"

def capitalize_words(string):
    """
    Функция принимает строку и делает заглавными первые буквы каждого слова в ней.
    :param string: строка
    :return: строка с заглавными первыми буквами каждого слова
    """
    return ' '.join(word.capitalize() for word in string.split())

# Пример использования

print(capitalize_words("hello world")) # Hello World
print(capitalize_words("the quick brown fox")) # The Quick Brown Fox
print(capitalize_words("python is awesome")) # Python Is Awesome

help(capitalize_words)