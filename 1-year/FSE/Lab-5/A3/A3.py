import sys

data = input("Введите входные данные: ")
res = str()
for word in data.split():
    if len(word) > 2:
        res += word[0]
print(res)