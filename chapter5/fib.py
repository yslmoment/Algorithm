# 피보나치 수열 분할 정복 알고리즘

def fib(n) :
  if n == 0 :
    return 0
  elif n == 1 :
    return 1
  else :
    return fib(n-1) + fib(n-2)
  
def fib_iter(n) :
  if (n < 2): 
    return n
  fib2 = 0
  fib1 = 1

  for i in range(2, n+1) :
    fib = fib1 + fib2
    fib2 = fib1
    fib1 = fib
  return fib

print('Fibonacci순환(6) = ', fib(6))
print('Fibonacci반복(6) = ', fib_iter(6))