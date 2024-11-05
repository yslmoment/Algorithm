def counting_sort(A):
  output = [0] * len(A) # 정렬 결과저장용 임시 리스트
  count = [0] * MAX_VAL # 각 숫자의 빈도를 저장
  for a in A: # 각 숫자별 빈도를 계산
    count[a] += 1
  for i in range(1, MAX_VAL): # count[i]가 출력 배열에서
    count[i] += count[i-1] # 해당 숫자의 위치가 되도록 수정
  for i in range(len(A)): # 모든 입력항목 A[i]에 대해
    count[A[i]] -= 1 # 킷값 A[i]의 위치를 하나 줄임
    output[count[A[i]]] = A[i] # 해당 위치에 A를 저장
  for i in range(len(A)): # 정렬 결과를 원래 배열에 복사
    A[i] = output[i]

MAX_VAL = 10
data = [ 1, 4, 1, 2, 7, 5, 2, 0] # 기존의 data 0을 추가
print("Original : ", data)
counting_sort(data)
print("Counting : ", data)
