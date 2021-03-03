def f6():
  a, b = map(int, input("Enter a and b: ").split())
  index = 1
  while a < b:
    print(str(index) + "-й день: " + "{:.2f}".format(a))
    index += 1
    a += (a * 0.1)
  print(str(index) + "-й день: " "{:.2f}".format(a))
  print("Ответ: на " + str(index) + "-й день спортсмен достиг результата — не менее " + str(b) + " км")