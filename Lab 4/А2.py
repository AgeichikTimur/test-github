text = ("He jests at scars.   That never felt a wound!  " "Hello, friend!  Are you OK?")
sentences = []
current = ""
for char in text:
    current += char
    if char in ".!?":
        # strip() убирает лишние пробелы и переносы строк по краям
        sentences.append(current.strip())
        current = ""

for s in sentences:
    print(s)

print("Предложений в тексте:", len(sentences))