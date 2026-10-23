import sys
number = 3 ** 9090001
bytes = sys.getsizeof(number)
print("Точный размер числа в байтах: ", bytes)
megabytes = bytes/ 1024 / 1024
print("Размер в мегабайтах:  ",megabytes)
