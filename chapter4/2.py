def insertion_sort(A, n) :
  if n > 1:
    insertion_sort(A, n - 1)
    key = A[n - 1] # A[n-1]을 끼워 넣기
    j = n - 2
    while j >= 0 and A[j] > key:
      A[j + 1] = A[j] # 항목들을 오른쪽으로 한 칸씩 이동
      j = j - 1 # 위치를 왼쪽으로 이동
    A[j + 1] = key
    
data = [ 5, 3, 8, 4, 9, 11 ,10, 1, 6, 2, 7 ]
print(" Original:", data)
insertion_sort(data, len(data))
print("Insertion:", data)