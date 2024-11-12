def find_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    
    if high - low == 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    
    mid = (low + high) // 2
    min1, max1 = find_min_max(arr, low, mid)
    min2, max2 = find_min_max(arr, mid + 1, high)
    
    return min(min1, min2), max(max1, max2)

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

print("Array:", arr)

min_val, max_val = find_min_max(arr, 0, n - 1)
print(f"Minimum value: {min_val}")
print(f"Maximum value: {max_val}")
