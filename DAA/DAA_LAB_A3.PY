import time
def merge(arr,left,mid,right):
    n1 = mid - left + 1
    n2 = right-mid
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
         L[i] = arr [left + i]

    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  
    j = 0  
    k = left  

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
def merge_sort(arr,left,right):
    if left >= right:
        return
    mid = (left + right)//2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)

import random
n = int(input("Enter the value of n: "))
arr = [random.randint(0, 10000) for _ in range(n)]

print("The array before sorting is:")
print(arr)

start_time = time.time()
merge_sort(arr, 0, n - 1)
end_time = time.time()

print("The sorted array is:")
print(arr)
print("The time taken to sort the array is:", end_time - start_time, "seconds")
