"""
In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.

Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.



Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation:
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.


Note:

1 <= persons.length = times.length <= 5000
0 <= persons[i] <= persons.length
times is a strictly increasing array with all elements in [0, 10^9].
TopVotedCandidate.q is called at most 10000 times per test case.
TopVotedCandidate.q(int t) is always called with t >= times[0].
"""
class TopVotedCandidate(object):
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.times = times
        self.maxperson = persons[[0]]
        self.maxvote = [1]
        self.rec = {persons[0]:1}
        for i in range(1, len(times)):
            if persons[i] in self.rec:
                self.rec[persons[i]] += 1
            else:
                self.rec[persons[i]] = 1
            if self.rec[persons[i]] >= self.maxvote[i-1]:
                self.maxvote.append(self.rec[persons[i]])
                self.maxperson.append(persons[i])
            else:
                self.maxvote.append(self.maxvote[i-1])
                self.maxperson.append(self.maxperson[i-1])

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        def bSearch(arr, target):
            i = 0
            j = len(arr)
            while i < j:
                mid = (i+j) / 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    i = mid + 1
                else:
                    j = mid
            return i

        index = bSearch(self.times, t)
        if index < len(self.times) and self.times[index] == t:
            index = index
        else:
            index -= 1
        return self.maxperson[index]


