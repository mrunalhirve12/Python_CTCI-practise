def SelectionSort(arr):
    for i in range(len(arr)):
         min_idx = i
         for j in range(len(arr)):
             if arr[min_idx] > arr[j]:
                 min_idx = j
    arr[min_idx], arr[i] = arr[i], arr[min_idx]