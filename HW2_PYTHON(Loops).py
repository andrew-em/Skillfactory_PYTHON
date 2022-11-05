
tickets = int(input("Введите количество билетов: "))

total_price = []
list_age =[]

for ticket in range(tickets):
    age_input = int(input("Введите ваш возраст: "))
    list_age.append(age_input)

for age in list_age:
    if age < 18:
        pass
    if  age <= 25 and age >= 18:
        total_price.append(990)
    if age > 25:
        total_price.append(1980)

if tickets > 3:
    print("Сумма к оплате с учетом скидки 10% :", int(sum(total_price) * 0.9), "рублей")
else:
    print("Сумма к оплате:", sum(total_price), "рублей")
