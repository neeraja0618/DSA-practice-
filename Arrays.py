#finding max element 
arr=[3,1,4,5,6,7]
max_val=arr[0]
for num in arr:
  if num>max_val:
    max_val=num
print("max element:",max_val)


#reversing array without slicing
arr = [1, 2, 3, 4, 5]
left = 0
right = len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print("Reversed array:", arr)

#second largest element
arr = [10, 5, 8, 20, 15]
largest = second = -1
for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Second largest:", second)
