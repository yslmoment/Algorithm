def quick_sort(A,left,right): # A[left...right]를 오름차순으로 정렬
  if left<right:     # 정렬 범위가 2개 이상인 경우 
    mid = partition(A,left,right)   # 좌우로 분할
    quick_sort(A,left,mid-1)  # 왼쪽 부분리스트를 퀵 정렬
    quick_sort(A,mid+1,right)   # 오른쪽 부분리스트를 퀵 정렬
  
def partition(A, left, right) :
  low = left + 1 # 왼쪽 부분 리스트의 인덱스 (증가방향)
  high = right # 오른쪽 부분 리스트의 인덱스 (감소방향)
  pivot = A[left] # 피벗 설정
  while (low <= high) : # low와 high가 역전되지 않는 한 반복
    while low <= right and A[low] < pivot : 
      low += 1
    while high >= left and A[high]> pivot : 
      high -= 1
    if low < high : # 선택된 두 레코드 교환
      A[low], A[high] = A[high], A[low]
    
  A[left], A[high] = A[high], A[left] # 마지막으로 high와 피벗 항목 교환
  return high # 피벗의 위치 반환

data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ] # 입력 리스트
print("Original : ", data)
quick_sort(data, 0, len(data)-1) # 퀵 정렬
print("QuickSort : ", data)
