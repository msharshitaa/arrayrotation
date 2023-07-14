def rotate_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
array = list(map(int, input().split()))
k = int(input())
size = len(array)

if k > size:
    k = k % size
rotate_array(array, 0, size - 1)
rotate_array(array, 0, k - 1)
rotate_array(array, k, size - 1)
print(array)
