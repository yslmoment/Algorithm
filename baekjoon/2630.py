import sys

# 입력 부분: 전체 종이의 크기 N을 입력받고, 각 행의 색종이 정보를 읽어서 2차원 리스트로 저장
N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

# 결과를 저장할 리스트, 하얀색(0)과 파란색(1)의 색종이 개수를 구하기 위함
result = []

# 분할정복을 이용한 재귀 함수
def solution(x, y, N):
    # 현재 구역의 첫 번째 위치의 색깔 저장 (하얀색: 0, 파란색: 1)
    color = paper[x][y]

    # 주어진 구역이 모두 같은 색인지 확인하기 위한 반복문
    for i in range(x, x + N):
        for j in range(y, y + N):
            # 만약 하나라도 다른 색이 있으면, 현재 구역을 4등분하여 재귀적으로 탐색
            if color != paper[i][j]:
                # 왼쪽 위 부분 (1사분면)
                solution(x, y, N // 2)
                # 오른쪽 위 부분 (2사분면)
                solution(x, y + N // 2, N // 2)
                # 왼쪽 아래 부분 (3사분면)
                solution(x + N // 2, y, N // 2)
                # 오른쪽 아래 부분 (4사분면)
                solution(x + N // 2, y + N // 2, N // 2)
                return  # 4등분하여 재귀적으로 탐색했으므로, 현재 함수는 종료

    # 주어진 구역이 모두 같은 색인 경우, 그 색깔을 결과 리스트에 추가
    if color == 0:
        result.append(0)  # 하얀색인 경우
    else:
        result.append(1)  # 파란색인 경우

# 전체 종이를 탐색하기 위해 재귀 함수 호출
solution(0, 0, N)

# 결과 리스트에서 하얀색(0)의 개수와 파란색(1)의 개수를 출력
print(result.count(0))
print(result.count(1))
