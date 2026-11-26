packets = input("Введите последовательность пакетов: ")

# Проверка длины и допустимых символов по подсказке 1
if len(packets) < 5:
    print("Неверный ввод. Длина строки должна быть не меньше 5!")
elif not all(char in '01' for char in packets):
    print("Неверный ввод. Используйте только символы '0' и '1'!")
else:
    total = len(packets)
    lost = packets.count('0') # Подсчет нулей по подсказке 2
    
    # Поиск самой длинной цепочки нулей по подсказке 3
    max_lost = 0
    current_lost = 0
    for packet in packets:
        if packet == '0':
            current_lost += 1
            if current_lost > max_lost:
                max_lost = current_lost
        else:
            current_lost = 0
            
    percent = (lost / total) * 100
    
    if percent <= 1:
        quality = "отличное"
    elif percent <= 5:
        quality = "хорошее"
    elif percent <= 10:
        quality = "удовлетворительное"
    elif percent <= 20:
        quality = "плохое"
    else:
        quality = "критическое состояние сети"
    print(f"Общее количество пакетов: ", total)
    print(f"Количество потерянных пакетов: ",lost)
    print(f"Длина самой длинной последовательности потерянных пакетов: ", max_lost)
    print(f"Процент потерь: {percent:.1f}%")
    print(f"Качество связи: ", quality)
