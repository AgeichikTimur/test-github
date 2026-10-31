x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
if (x1 + y1) % 2 == 0:
    color1 = "White"
else:
    color1 = "Black"

if (x2 + y2) % 2 == 0:
    color2 = "White"
else:
    color2 = "Black"

if color1 == color2:
    print("YES")
    print(color1)
else:
    print("NO")
