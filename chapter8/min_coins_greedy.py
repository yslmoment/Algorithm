def min_coins_greedy( coins, V ):
  count = [] 
  for i in range(len(coins)) :
    cnt = V // coins[i] 
    count.append(cnt)
    V -= cnt * coins[i] 
  return count

coins = [500 , 100 , 50 , 10 , 5 , 1]
V = 1000
print("잔돈 액수 = ", V)
print("동전 종류 = ", coins)
print("동전 개수 = ", min_coins_greedy(coins, V ))