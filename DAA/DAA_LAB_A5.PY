def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

n = int(input("Enter the number of elements: "))
print("Enter the elements: ")
arr = list(map(int, input().split()))
print("The unsorted list is:")
print(arr)
insertion_sort(arr)
print("The sorted list is:")
print(arr)
