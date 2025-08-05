def bubble_sort(arr):
    n = len(arr)

    for i in (n):
        for j in (n-1-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



arr = [55 ,7, 78 ,12, 42]
print(bubble_sort(arr))

def selection_sort(arr):
    n = len(arr) # 배열의 길이

    # 첫번째 원소부터 최소값을 찾자
    for i in range(n-1): # 최소값을 찾는 행위를 반복한다.
        min_idx = i # 최소값의 인덱스 겸 최소값을 탐색하는 시작지점
        for j in range(i+1):
            # 현재까지의 최소값보다 작은 값이 발견되면
            # 최소값 인덱스를 갱신한다.
            if arr[j] < arr[min_idx]:
                min_idx = j
        # for문이 끝났다 = 끝까지 돌아서 최소값을 찾았다
        arr[i], arr[min_idx] = arr[min_idx], arr[i