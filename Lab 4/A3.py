text = input("Введите текст: ")
words = text.split()
abb = ""
for word in words:
    if len(word) >= 3:
        abb += word[0].upper()

print("Аббревиатура:", abb)