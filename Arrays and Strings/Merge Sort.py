def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        l = mergeSort(arr[:mid])
        r = mergeSort(arr[mid:])

        mergeSort(l)
        mergeSort(r)

        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = arr[i]
                i += 1
            else:
                arr[k] = arr[j]
                j += 1
            k += 1


        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[i]
            j += 1
            k += 1
