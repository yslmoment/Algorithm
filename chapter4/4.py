# 이진 탐색 (순환)
def binary_search(A, key, low, high) :
  if (low <= high) : # 항목들이 남아 있으면(종료 조건)
    mid = (low + high) // 2 # 정수 나눗셈 // : 몫을 반환
    if key == A[mid] : # 탐색 성공
      return mid # 인덱스 반환
    elif key < A[mid] : # 왼쪽 부분 리스트 탐색
      return binary_search(A, key, low, mid-1)
    else : # 오른쪽 부분 리스트 탐색
      return binary_search(A, key, mid+1, high)
  return -1 # 탐색 실패: -1 반환

# 이진 탐색 (반복)
def binary_search_iter(A, key, low, high) :
  while (low <= high) : # 항목들이 남아 있으면(종료 조건)
    mid = (low + high) // 2
    if key == A[mid]: # 탐색 성공
      return mid # 인덱스 반환
    elif key > A[mid]: # key가 mid의 값보다 크면
      low = mid + 1 # mid+1 ~ high 사이 검색
    else: # key가 mid의 값보다 작으면
      high = mid - 1 # low ~ mid-1 사이 검색
  return -1 # 탐색 실패

listA = [1, 3, 8, 13, 13, 16, 21, 26, 27, 30, 33, 36, 39, 41, 44, 49]
print("입력 리스트 =", listA)
print("8 탐색(순환) -->", binary_search(listA, 8, 0, len(listA)-1) )
print("8 탐색(반복) -->", binary_search_iter(listA, 8, 0, len(listA)-1) )
print("25 탐색(순환) -->", binary_search(listA, 25, 0, len(listA)-1) )
print("25 탐색(반복) -->", binary_search_iter(listA, 25, 0, len(listA)-1) )