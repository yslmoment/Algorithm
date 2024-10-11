import random

# 1) 100~300 사이의 난수를 100개 생성
random_numbers = [random.randint(100, 300) for _ in range(100)]

# 2) 삽입 정렬 알고리즘을 사용하여 숫자들을 정렬
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # 현재 값보다 큰 요소를 한 칸씩 뒤로 이동
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 정렬된 리스트
sorted_numbers = insertion_sort(random_numbers)

# 보간 탐색 함수
def interpolation_search(arr, low, high, key):
    while low <= high and key >= arr[low] and key <= arr[high]:
        # 보간 탐색의 중간값 계산
        if low == high:
            if arr[low] == key:
                return low
            return -1
        
        mid = low + int((high - low) * (key - arr[low]) / (arr[high] - arr[low]))

        # 중간값과 키 값 비교
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:  # 키가 더 크면 상위 부분을 탐색
            low = mid + 1
        else:  # 키가 더 작으면 하위 부분을 탐색
            high = mid - 1
    
    return -1  # 요소가 없으면 -1 반환

# 이진 탐색 함수 정의
def binary_search(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2  # 중간값 계산

        # 중간값과 키 값 비교
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:  # 키가 더 크면 상위 부분을 탐색
            low = mid + 1
        else:  # 키가 더 작으면 하위 부분을 탐색
            high = mid - 1
    
    return -1  # 요소가 없으면 -1 반환

# 보간 탐색 키 목록과 이진 탐색 키 목록
interpolation_keys = [110, 120, 150, 200, 250, 123, 299]
binary_keys = [110, 120, 150, 200, 250, 123, 299]

# 각 키에 대한 보간 탐색 수행
interpolation_results = {key: interpolation_search(sorted_numbers, 0, len(sorted_numbers) - 1, key) for key in interpolation_keys}

# 각 키에 대한 이진 탐색 수행
binary_results = {key: binary_search(sorted_numbers, 0, len(sorted_numbers) - 1, key) for key in binary_keys}

# 결과 출력
print("정렬된 숫자 리스트:", sorted_numbers)
print("\n보간 탐색 결과:")
for key, index in interpolation_results.items():
    if index != -1:
        print(f"키 {key}는 인덱스 {index}에 있습니다.")
    else:
        print(f"키 {key}는 리스트에 없습니다.")

print("\n이진 탐색 결과:")
for key, index in binary_results.items():
    if index != -1:
        print(f"키 {key}는 인덱스 {index}에 있습니다.")
    else:
        print(f"키 {key}는 리스트에 없습니다.")


