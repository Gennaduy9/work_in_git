# Что еще добавить, чтобы спровоцировать конфликт м между ветками

def uppercase_string(input_string):
    """
    Функция которая принимает на вход строку и возвращает ее в верхнем регистре.
    :return: строка с заглавными буквами в каждом слове
    """
    return input_string.upper()

# Пример использования

string = "Hello, World!"
upper_string = uppercase_string(string)
print(f"{upper_string}\n") # выводит "HELLO, WORLD!"

def capitalize_words(string):
    """
    Функция принимает строку и делает заглавными первые буквы каждого слова в ней.
    :return: строка с заглавными первыми буквами каждого слова
    """
    return ' '.join(word.capitalize() for word in string.split())

# Пример использования

print(capitalize_words("hello world")) # Hello World
print(capitalize_words("the quick brown fox")) # The Quick Brown Fox


help(capitalize_words)
help(uppercase_string)

def file(a, b):
    """
    Функцию, которая складывает два числа
    """
    return a + b

