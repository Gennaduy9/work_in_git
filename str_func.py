def capitalize_words(string):
    """
    Функция принимает строку и делает заглавными первые буквы каждого слова в ней.
    :return: строка с заглавными первыми буквами каждого слова
    """
    return ' '.join(word.capitalize() for word in string.split())

# Пример использования

print(capitalize_words("hello world")) # Hello World
print(capitalize_words("the quick brown fox")) # The Quick Brown Fox





