def calculate_change_count(price):
    change = 1000 - price  # 1000엔에서 물건 가격을 뺀 잔돈
    coins = [500, 100, 50, 10, 5, 1]  # 잔돈 단위
    count = 0

    for coin in coins:
        count += change // coin  # 각 동전으로 줄 수 있는 최대 개수를 더함
        change %= coin  # 나머지 잔돈 계산

    return count

price = int(input("물건 가격 : "))
print(calculate_change_count(price))
price = int(input("물건 가격 : "))
print(calculate_change_count(price))


