
def palin(n):
  s = str(n)
  s_length = len(s)
  result = True
  for i in range(s_length):
    if s[i] != s[s_length-i-1]: result = False
  return result

maxi = 0
for a in range(999,-1,-1):
  for b in range(999,-1,-1):
    if palin(a*b) and maxi < a*b: maxi = a*b
print maxi
