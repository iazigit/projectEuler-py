
coins = [200,100,50,20,10,5,2,1]

def print_coins(change):
  if change == 0: print "Nothing"
  else:
    for (n, c) in change:
      if n != 0: print "{}*{} + ".format(n,c), 
    total = sum(map(lambda (n, c): n*c, change))
    print " = " + str(total)

def make_change(n, usable_coins, coins_used): 
  if len(usable_coins) == 1 : 
    coins_used.append((n, 1))
    print_coins(coins_used)
    return 1 
  coin = usable_coins.pop(0)
  possibilities = 0
  for number in range(1, n/coin + 1):  
    used = list(coins_used)
    used.append((number, coin))
    possibilities +=  make_change(n - number*coin, list(usable_coins), used)
  possibilities += make_change(n, list(usable_coins), coins_used)
  return possibilities



print make_change(200, coins, list([]))
