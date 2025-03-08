#no of argument but only one expression
a = lambda b,c,d : b+c+d
print(a(3,4,5))
def ano(n):
  return lambda b : b * n
a = ano(2)
print(a(3))