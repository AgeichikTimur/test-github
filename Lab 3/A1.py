import random
import time
n = int(input("Введите количество примеров: "))
correct_count = 0
total_time = 0.0
for i in range(1, n + 1):
    print(f"Вопрос {i}/{n}")
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    start_time = time.time()
    while True:
        try:
            answer = int(input(f"{a} × {b} = "))
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")
    time_spent = time.time() - start_time
    total_time += time_spent
    if answer == a * b:
        print(f"Верно! (Время: {time_spent:.1f} сек)")
        correct_count += 1
    else:
        print(f"Неверно! Правильно: {a * b} (Время: {time_spent:.1f} сек)")
avg_time = total_time / n if n > 0 else 0
percent = (correct_count / n) * 100 if n > 0 else 0

print("=" * 50)
print("СТАТИСТИКА:")
print("=" * 50)
print(f"Общее время: {total_time:.1f} секунд")
print(f"Среднее время на вопрос: {avg_time:.1f} сек")
print(f"Правильных ответов: {correct_count}/{n}")
print(f"Процент правильных: {percent:.1f}%")
