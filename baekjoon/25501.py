import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 재귀 호출을 통한 판별 함수
def recursion(s, l, r):
    global cnt  # 전역 변수로 재귀 호출 횟수를 기록하기 위해 선언
    cnt += 1  # 함수가 호출될 때마다 재귀 호출 횟수 증가

    # 재귀 종료 조건: 왼쪽 인덱스가 오른쪽 인덱스 이상이 되면 재귀문임을 확인
    if l >= r:
        return 1  # 재귀문일 경우 1문 반환
    # 현재 왼쪽과 오른쪽의 문자가 다르면 재귀문이 아님
    elif s[l] != s[r]:
        return 0  # 재귀문이 아닐 경우 0 반환
    # 현재 인덱스가 같다면 재귀적으로 다음 인덱스를 확인
    return recursion(s, l + 1, r - 1)

# 재귀문인지 판별하는 함수: 문자열 s를 받아서 재귀 함수를 호출
def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)

# 테스트할 문자열 개수를 입력 받음
N = int(input().strip())

print("")

# 여러 테스트 케이스 처리
for _ in range(N):
    cnt = 0  # 각 문자열에 대해 재귀 호출 횟수를 초기화
    # 문자열 입력을 받고, isPalindrome 함수로 회문 여부와 호출 횟수를 출력
    print(isPalindrome(input().rstrip()), cnt)  # .rstrip()으로 줄바꿈 문자 제거
