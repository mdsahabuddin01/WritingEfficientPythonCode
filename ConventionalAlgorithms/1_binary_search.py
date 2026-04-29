def binary_search(lst, n):
  low = 0
  high = len(lst) - 1
  while low <= high:
    mid = low + (high - low) // 2
    if lst[mid] == n:
      return mid
    elif lst[mid] < n:
      low = mid + 1
    else:
      high = mid - 1

  return -1



list = [1,2,3,4,5,6,7,8,9,10]
x = 5
result = binary_search(list, x)
if result != -1:
  print("Element is present at index: ", result)
else:
  print("Element is not present in array.")
