NO_OF_CHARS = 128
def shift_table(pat):
  m = len(pat) # 패턴의 길이
  tbl = [m]*NO_OF_CHARS # 시프트 테이블. 패턴의 길이로 초기화

  for i in range(m-1): # 패턴의 모든(마지막을 제외) 문자에 대해
    tbl[ord(pat[i])] = m-1-i # 문자가 끝에서 앞으로 패턴의 몇 번째인지
  return tbl

def search_horspool(T, P):
  m = len(P) # 패턴의 길이
  n = len(T) # 텍스트(입력)의 길이
  t = shift_table(P) # shift 테이블 생성
  i = m-1 # i는 텍스트의 위치(우측끝)
  while i < n : # 가능한 모든 위치에 대해
    k = 0 # 매칭된 문자 수
    while k < m and P[m-1-k]==T[i-k]: # 뒤에서 앞으로
      k += 1 # 맞으면 계속 앞으로 진행
    if k == m : # 매칭성공: 매칭위치(왼쪽) 반환
      return i-m+1
    else : # 매칭실패
      tc = t[ord(T[i-k])]
      i += max(1, tc - k) # T[i]의 테이블 참조 --> 건너뜀
  return -1 # 매칭실패 –1 반환

P = "MANGO"
t = shift_table(P)
for i in range(len(t)):
  if t[i] != len(P):
    print(chr(i), ":", t[i], end="; ")

print("패턴의 위치 :", search_horspool("APPLEMANGOBANANAGRAPE", P))

