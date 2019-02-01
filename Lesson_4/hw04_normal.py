# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import re

# 1
line = "rfRFTGFdDRFTfdscfsCggtGTGdSSCgVGGETFsdcGVGfcDFCGCGbgbCf"
print(re.findall("[a-z]+", line))


# 2
lst = []

b = ""

for i in line:
    if i.islower():
        b += i
    elif i.isupper() and len(b) > 0:
        lst.append(b)
        b = ""
if len(b) > 0:
    lst.append(b)

print(lst)



# Задание-2:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random
import re

lst = [random.randint(0, 9) for _ in range(2500)]
number = ''.join(str(el) for el in lst)

with open("test.txt", "w", encoding="UTF-8") as f:
    f.write(number)
f.close()

with open("test.txt", "r", encoding="UTF-8") as f:
    number = f.read()
f.close()

a = []
b = []

for i in range(10):
    pattern = str(i) + "+"
    a.append(max(re.findall(pattern, number)))


count = max([len(i) for i in a])

for el in a:
    if len(el) == count:
        b.append(el)

print(f"Самые длинные последовательности одинаковых цифр длинной: {count}: {b}")

