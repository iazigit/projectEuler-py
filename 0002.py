fibo2 = 1
fibo1 = 1
sum = 0
while fibo2 < 4000000:
  print fibo2
  if fibo2 % 2 == 0: sum += fibo2
  aux = fibo1
  fibo1 = fibo2
  fibo2 = aux+fibo2
print sum
