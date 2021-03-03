def f5():
  income, cost = map(float, input("Ввод выручки и издержек фирмы: ").split())

  if income > cost:
    print("Прибыль")
    profit = income - cost
    print("Рентабельность выручки: " + str(profit / income))
    employees = int(input("Ввод численность сотрудников: "))
    print("Прибыль на одного сотрудника: " + str(profit/employees))
  else:
    print("Издержек")