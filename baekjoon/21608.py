# 상어 초등학교 
n = int(input())  # 정수 n 입력 받기 (학교의 크기 n x n)
data = [[0] * n for _ in range(n)]  # n x n 크기의 학교 좌석 배열 초기화
students = [list(map(int, input().split())) for _ in range(n**2)]  
# n^2명의 학생과 그들의 선호하는 학생들 정보 입력 받기

# 방향 벡터 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 모든 학생들에 대해 자리 배정을 수행
for student in students:
    available = []  # 가능한 자리 목록을 저장할 리스트

    # 모든 좌석을 순회
    for i in range(n):
        for j in range(n):
            if data[i][j] == 0:  # 해당 좌석이 비어있는 경우
                prefer, empty = 0, 0  # 선호하는 학생 수와 빈 자리 수 초기화
                
                # 인접한 네 방향을 검사
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                     
                    if 0 <= nx < n and 0 <= ny < n:  # 범위 안에 있을 경우
                        if data[nx][ny] in student[1:]:  # 인접한 칸에 선호하는 학생이 있는 경우
                            prefer += 1
                        if data[nx][ny] == 0:  # 인접한 칸이 비어있는 경우
                            empty += 1

                available.append((i, j, prefer, empty))  # 후보 리스트에 추가
    
    # 가능한 자리 중에서 선호하는 학생 수가 많고, 그 후로는 빈 자리 수가 많은 순으로 정렬하며, 행과 열이 작은 순서대로 정렬
    available.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    data[available[0][0]][available[0][1]] = student[0]  # 최적의 자리에 학생 배치

# 최종 만족도 점수 계산
answer = 0
score = [0, 1, 10, 100, 1000]  # 만족도에 따른 점수 배열
students.sort()  # 학생 정보를 정렬

# 각 자리마다 만족도 점수 계산
for i in range(n):
    for j in range(n):
        count = 0  # 주변에 선호하는 학생 수 카운트

        # 주변 네 방향 검사
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < n:  # 범위 안에 있을 경우
                if data[nx][ny] in students[data[i][j] - 1]:  # 주변에 선호하는 학생이 있는 경우
                    count += 1

        answer += score[count]  # 해당 자리의 만족도 점수를 총합에 추가

print(answer)  # 최종 점수 출력