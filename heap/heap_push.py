# 배열 heap에 저장된 최대 힙에 노드 n을 삽입하는 함수
def heappush(heap, n) :
  heap.append(n) # 맨 마지막 노드로 일단 삽입
  i = len(heap)-1 # 노드 n의 위치
  while i != 1 : # n이 루트가 아니면 up-heap 진행
    pi = i//2 # 부모 노드의 위치
    if n <= heap[pi]: # 부모보다 작으면 up-heap 종료
      break
    heap[i] = heap[pi] # 부모를 끌어내림
    i = pi # i가 부모의 인덱스가 됨
  heap[i] = n # 마지막 위치에 n 삽입
  return n

# 최대힙 heap에서 최대 노드를 꺼내 반환하는 함수
def heappop(heap) :
  size = len(heap) - 1 # 노드의 개수
  if size == 0 : # 공백상태
    return None
  root = heap[1] # 삭제할 루트 노드
  last = heap[size] # 마지막 노드
  pi = 1 # 부모 노드의 인덱스
  i = 2 # 자식 노드의 인덱스
  while (i <= size): # 마지막 노드 이전까지
    if i<size and heap[i] < heap[i+1]: # right가 더 크면 i를 1 증가
      i += 1 # 비교할 자식은 오른쪽 자식
    if last >= heap[i]: # 자식이 더 작으면 down-heap 종료
      break
    heap[pi] = heap[i] # 아니면 down-heap 계속
    pi = i
    i *= 2

  heap[pi] = last # 맨 마지막 노드를 parent위치에 복사
  heap.pop() # 맨 마지막 노드 삭제
  return root # 저장해두었던 루트를 반환

def heapSort(data) :
  heap = [0]
  for e in data : # 모든 데이터를 최대 힙에 삽입  
    heappush(heap, e)
  for i in range(1, len(data)+1) : #모든 데이터를 힙에서 꺼내 역순으로 저장
    data[-i] = heappop(heap) # 음수 인덱스: -1, -2, ...,-n

data = [7, 5, 4, 8, 9, 3, 2, 3] # 힙에 삽입할 데이터
heap = [0]
print("입력: ", data)
for e in data : # 모든 데이터를 힙에 삽입
  heappush(heap, e); print("heap: ", heap[1:]) # index 0는 제외

print("삽입: ", heappush(heap,13))
print("heap: ", heap[1:])
print("삭제: ", heappop(heap))
print("heap: ", heap[1:])
heapSort(data)
print("정렬: ", data)