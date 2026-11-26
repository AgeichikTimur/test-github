x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

if x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0:
    print("Yes, 1 четверть")
elif x1 < 0 and y1 > 0 and x2 < 0 and y2 > 0:
    print("Yes, 2 четверть")
elif x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0:
    print("Yes, 3 четверть")
elif x1 > 0 and y1 < 0 and x2 > 0 and y2 < 0:
    print("Yes, 4 четверть")
else:
    print("No")
