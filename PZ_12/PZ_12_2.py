# Из заданной строки отобразить только символы нижнего регистра. Использовать библиотеку string.
# Строка 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'.

import string

text = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
lowercase_chars = filter(lambda c: c in string.ascii_lowercase, text)
result = ''.join(lowercase_chars)
print(result)
