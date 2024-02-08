sum = 0
tickets = int(input("Введите количество билетов:"))
age = int(input("Введите возраст:"))
for tickets in range(tickets):
   if age < 18:
      sum += 0
   elif 18 <= age <= 25:
      sum += 990
   elif age > 25:
      sum += 1390

if tickets > 3:
   sum -= sum / 100 * 10
print("Сумма к оплате", sum)



