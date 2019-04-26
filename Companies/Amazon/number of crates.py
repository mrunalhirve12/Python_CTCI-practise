import heapq
import math


def dist(total, arr, capacity):
    if not total or not capacity:
        return []
    dict = {}
    for i in range(len(arr)):
        val = (arr[i][0]**2) if arr[i][0] else 0 + (arr[i][-1]**2) if arr[i][0] else 0
        dist = math.sqrt(val)
        diff = abs(capacity - dist)
        dict[(arr[i][0],arr[i][-1])] = diff
    heap = [(value, key) for key, value in dict.items()]
    if capacity <= total:
        smallest = heapq.nsmallest(capacity, heap)
        result = [list(key) for value, key in smallest]
    else:
        smallest = heapq.nsmallest(total, heap)
        result = [list(key) for value, key in smallest]
    return result


arr = [[1], [3,4], [1]]
print(dist(3,arr,1))