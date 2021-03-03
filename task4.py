def f4():
  num = int(input("Вводит целое положительное число: "))
  n_max = num % 10
  num //= 10
  while num > 0:
    n = num %10
    num //= 10
    if n > n_max:
      n_max = n

  return "Самая большая цифра: " + str(n_max)