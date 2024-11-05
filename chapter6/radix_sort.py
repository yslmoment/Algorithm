from queue import Queue # 파이썬 queue모듈의 Queue 사용
def radix_sort(A) :
  queues = [] # 큐의 리스트
  for i in range(BUCKETS) :
    queues.append(Queue()) # BUCKETS개의 큐 사용

  n = len(A)
  factor = 1 # 1의 자리부터 시작
  for d in range(DIGITS) : # 모든 자리에 대해
    for i in range(n) : # 자릿수에 따라 큐에 삽입
      queues[(A[i]//factor) % BUCKETS].put(A[i]) # 숫자를 삽입
    j = 0
    for b in range(BUCKETS) : # 버킷에서 꺼내어 리스트 A로
      while not queues[b].empty() : # b번째 큐가 공백이 아닌 동안
        A[j] = queues[b].get() # 원소를 꺼내 리스트에 저장
        j += 1
    factor *= BUCKETS # 다음 자리수로 간다.
    print("step", d+1, A) # 중간 과정 출력용 문장

import random # 테스트를 위한 난수 발생을 위해 random 모듈 포함
BUCKETS = 10 # 10진법으로 정렬
DIGITS = 3 # 최대 3 자릿수
data = []
for i in range(10) :
  data.append(random.randint(1,999)) # 1~9999사이의 숫자 10개 생성
radix_sort(data) # 기수 정렬
print("Radix:", data) # 결과 출력

