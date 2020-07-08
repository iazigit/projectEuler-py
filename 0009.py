
for a in range(999):
  for b in range(999):
    c = 1000 - a - b
    if c*c == (a*a + b*b): print a*b*c
