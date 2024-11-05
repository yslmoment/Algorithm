M = 97
def hashFn(key):
    sum = 0
    for c in key:
        sum += ord(c)
    hash_value = sum % M
    print(f"The hash value of '{key}' is {hash_value}")  # 출력문 추가
    return hash_value

# 예시로 함수를 사용해보기
hashFn("example")  # 'example' 문자열의 해시값을 출력


