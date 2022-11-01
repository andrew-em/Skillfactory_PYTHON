money = int(input("Введите желаемый депозит: "))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}


income_TKB = int(per_cent.get('ТКБ')*money/100)
income_SKV = int(per_cent.get('СКБ')*money/100)
income_BTV = int(per_cent.get('ВТБ')*money/100)
income_SBER = int(per_cent.get('СБЕР')*money/100)

total_income = [income_TKB, income_SKV, income_BTV, income_SBER]
print(total_income)

max_income = max(total_income)
print("Максимальный доход:", max_income)




