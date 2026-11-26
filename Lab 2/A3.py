pred = int(input())
nast = int(input())
if nast >= pred:
    gas = nast - pred
else:
    gas = (10000 - pred) + nast
if gas <= 300:
    cost = 21.0
elif gas <= 600:
    cost = 21.0 + (gas - 300) * 0.06
elif gas <= 800:
    cost = 39.0 + (gas - 600) * 0.04
else:
    cost = 47.0 + (gas - 800) * 0.025
avg_price = cost / gas

print("Предыдущее:", pred)
print("Текущее:", nast)
print("Использовано:", gas)
print("К оплате:", round(cost, 2))
print("Ср. цена m^3:", round(avg_price, 2))
