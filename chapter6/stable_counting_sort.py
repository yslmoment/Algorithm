def stable_counting_sort_by_y(coords):
    MAX_Y = max(coords, key=lambda x: x[1])[1] + 1  # y의 최대값을 구하고 +1
    output = [None] * len(coords)  # 정렬 결과를 저장할 리스트
    count = [0] * MAX_Y  # y 값을 카운트할 배열

    # y 값을 카운트
    for _, y in coords:
        count[y] += 1

    # 누적 합을 계산
    for i in range(1, MAX_Y):
        count[i] += count[i - 1]

    # 입력 배열을 순회하며 각 요소를 출력 배열에 올바른 위치에 배치
    for x, y in reversed(coords):  # 뒤에서부터 순회하면서 안정성 유지
        output[count[y] - 1] = (x, y)
        count[y] -= 1  # 사용된 위치는 감소

    return output

# 예시 데이터
data = [(1, 3), (2, 1), (3, 2), (4, 3), (5, 1)]
sorted_data = stable_counting_sort_by_y(data)
print("Original:", data)
print("Sorted by y:", sorted_data)

