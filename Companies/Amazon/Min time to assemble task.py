import heapq


def minTime(npparts, parts):
        if npparts == 0:
            return 0
        if len(parts) == 1:
            return parts[0]
        heap = parts
        #heapify heap
        heapq.heapify(heap)
        val = 0
        res = 0
        result = 0
        #chk for remaining elements
        for i in range(2):
            while len(heap) > 1:
                val1 = heapq.heappop(heap)
                val2 = heapq.heappop(heap)
                result = val1 + val2
                heapq.heappush(heap, result)
                res += result
        return res

print(minTime(4,[8,4,6,12]))