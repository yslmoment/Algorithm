def knapSack_fractional_greedy(obj, W): # obj = [(물건,무게,가치),…]
  obj.sort(key = lambda o: o[2]/o[1], reverse=True) # 내림차순정렬
  
  totalValue = 0 # 전체 배낭의 가치
  for o in obj :
    if W <= 0 : # 용량이 다 찬 경우
      break 
    if W - o[1] >= 0: # 물건 전체가 들어갈 수 있는 경우
      W -= o[1] 
      totalValue += o[2]
    else: # 물건의 일부만 넣을 수 있는 경우
      fraction = W / o[1]
      totalValue += o[2] * fraction
      W = 0 # int(W - (o[1] * fraction))
  return totalValue

obj = [ ("A", 10, 80), ("B", 12, 120), ("C", 8, 60)] # (물건,무게,가치)
print("W = 36 ", obj)
print("부분적인배낭(36): ", knapSack_fractional_greedy(obj,36), end='\n')
obj = [ ("A", 10, 60), ("B", 40, 40), ("C", 20, 100), ("D", 30, 120) ]
print("W = 80 ", obj)
print("부분적인배낭(80): ", knapSack_fractional_greedy(obj, 80))