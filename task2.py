# Author: Vuong Truong Son and Vladislav Volkov
def f2():
  sec = int(input("Enter seconds: "))
  m, s = divmod(sec, 60)
  h, m = divmod(m, 60)
  return "{:02d}:{:02d}:{:02d}".format(h, m, s)