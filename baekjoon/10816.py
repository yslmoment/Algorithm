import sys

# 첫 번째 줄 입력: 정수 N을 받아서 N_s라는 리스트로 정렬된 상태로 저장
N = int(sys.stdin.readline().strip())
N_s = sorted(list(map(int, sys.stdin.readline().strip().split())))

# 두 번째 줄 입력: 정수 M을 받아서 M_s라는 리스트로 저장
M = int(sys.stdin.readline().strip())
M_s = list(map(int, sys.stdin.readline().strip().split()))

# N_s의 각 원소의 등장 횟수를 기록하기 위한 딕셔너리 생성
n_dic = {}
for n in N_s:
    if n in n_dic:
        n_dic[n] += 1  # 이미 존재하는 값이면 등장 횟수를 1 증가
    else:
        n_dic[n] = 1  # 새로운 값이면 등장 횟수를 1로 초기화

# 이진 탐색 함수 정의: m을 N_s에서 찾아 등장 횟수를 반환
def binary(m, N_s, start, end):
    if start > end:
        return 0  # 찾는 값이 없으면 0 반환
    mid = (start + end) // 2  # 중간 인덱스 계산
    if m == N_s[mid]:
        return n_dic[m]  # 찾는 값이 있으면 등장 횟수 반환
    elif m < N_s[mid]:
        return binary(m, N_s, start, mid - 1)  # 왼쪽 부분을 탐색
    else:
        return binary(m, N_s, mid + 1, end)  # 오른쪽 부분을 탐색

# M_s의 각 원소에 대해 이진 탐색을 수행하여 등장 횟수 출력
for m in M_s:
    print(binary(m, N_s, 0, len(N_s) - 1), end=' ')
