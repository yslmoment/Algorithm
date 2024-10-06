# 팩토리얼(하향식 축소 정복 기법)
def factorial_recur(n):
  if n==1:
    return 1
  else :
    return n*factorial_recur(n-1)

# 팩토리얼(상향식 축소 정복 기법)
def factorial_iter(n):
  result = 1
  for k in range(1, n + 1):
      result = result * k
  return result

num = int(input("input : "))
print(f"output(recur) : {factorial_recur(num)}")
print(f"output(iter) : {factorial_iter(num)}")