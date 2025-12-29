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


#bubble sort
arr = [5, 1, 4, 2]
for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("Sorted array:", arr)
