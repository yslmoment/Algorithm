import sys

# 터미널에서 입력을 받을 때, 공백으로 구분된 정수 6개를 입력받아 변수에 저장
# 예: a b c d e f (각각 연립방정식의 계수와 상수항에 해당)
a, b, c, d, e, f = map(int, input().strip().split())

# 가능한 x의 범위는 -999에서 999까지이므로, 해당 범위를 반복문으로 탐색
for x in range(-999, 1000):
    # 각 x에 대해 가능한 y의 범위를 -999에서 999까지 탐색
    for y in range(-999, 1000):
        # 첫 번째 방정식과 두 번째 방정식을 동시에 만족하는지 확인
        if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
            # 조건을 만족하는 (x, y)가 발견되면 출력하고 반복문 종료
            print(x, y)
            break
    # 첫 번째 for문에서도 (x, y)가 발견되면 종료하기 위해 추가적인 break
    else:
        continue
    break

