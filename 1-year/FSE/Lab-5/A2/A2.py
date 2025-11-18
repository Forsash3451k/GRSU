import re
import sys

data = input("Введите входные данные: ")
data = str(data)
sentences = re.split(r'(?<=[.?!]) +', data)
for sentence in sentences:
    print(sentence)
print(f"Предложений в тексте: {len(sentences)}")