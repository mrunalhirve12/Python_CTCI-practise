


def partition(arr, l, hi):
    i = l - 1
    pivot = arr[hi]
    for j in range(l, hi):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], arr[pivot] = arr[pivot], arr[i+1]
    return i+1

def quickSort(arr, l, hi):
    if l < hi:
        pi = partition(arr, l, hi)
        quickSort(arr, l, pi-1)
        quickSort(arr, pi+1, hi)