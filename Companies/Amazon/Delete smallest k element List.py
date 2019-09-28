import heapq


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def getMinKElements(self, nums, k, n):
            heap = []
            count = 1
            ptr = nums
            while ptr and count <= k:
                val = -(ptr.val - n)
                heap.append((val, ptr))
                ptr = ptr.next
                count += 1
            #heapify heap
            heapq.heapify(heap)
            #chk for remaining elements
            while ptr.next:
                if -(ptr.val-n) > heap[0][0]:
                    val = -(ptr.val-n)
                    heapq.heappushpop(heap, (val, ptr))
                ptr = ptr.next

            lists = []
            for i in range(k):
                lists.append(heapq.heappop(heap)[1])


            # Search for the key to be deleted, keep track of the
            # previous node as we need to change 'prev.next'
            while nums and lists is not None:
                temp = nums
                # If head node itself holds the key to be deleted
                if temp.val in lists:
                    nums = temp.next
                    lists.remove(temp.data)
                    break
                else:
                    while temp is not None:
                        if temp.val in lists:
                            prev.next = temp.next
                            lists.remove(temp.val)
                        prev = temp
                        temp = temp.next
            print(self.nums)









l1 = ListNode(3)
l1.next = ListNode(2)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(7)
l1.next.next.next.next = ListNode(1)
l1.next.next.next.next.next = ListNode(5)
l1.next.next.next.next.next.next = ListNode(4)

s = Solution()
s.getMinKElements(l1, 4, 3)