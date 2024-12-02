# 손익분기점
A, B, C = map(int, input().split())  # 고정 비용 A, 변동 비용 B, 판매 가격 C 입력 받음
if B >= C:
    print(-1)  # 변동 비용이 판매 가격보다 크거나 같으면 손익분기점 도달 불가능, -1 출력
else:
    print(int(A//(C-B)+1))  # 손익분기점을 계산하여 출력