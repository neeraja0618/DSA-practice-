#linear search
arr = [4, 7, 1, 9]
target = 7
found = False
for i in range(len(arr)):
    if arr[i] == target:
        found = True
        print("Element found at index", i)
        break
if not found:
    print("Element not found")


#binary search
arr = [2, 4, 6, 8, 10, 12]
target = 8
left = 0
right = len(arr) - 1
found = False
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        print("Element found at index", mid)
        found = True
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
if not found:
    print("Element not found")


#bubble sort
arr = [5, 1, 4, 2]
for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("Sorted array:", arr)


#selection sort
arr = [64, 25, 12, 22, 11]
for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
print("Sorted array:", arr)
