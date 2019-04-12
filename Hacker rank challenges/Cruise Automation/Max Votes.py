"""
Find winner of an election where votes are represented as candidate names
Given an array of names of candidates in an election. A candidate name in array represents a vote casted to the candidate. Print the name of candidates received Max vote. If there is tie, print lexicographically smaller name.

Examples:

Input :  votes[] = {"john", "johnny", "jackie",
                    "johnny", "john", "jackie",
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny",
                    "john"};
Output : John
We have four Candidates with name as 'John',
'Johnny', 'jamie', 'jackie'. The candidates
John and Johny get maximum votes. Since John
is alphabetically smaller, we print it.
"""
import sys
from collections import defaultdict
"""
NAIVE APPROACH: O(N2)
A simple solution is to run two loops and count occurrences of every word. Time complexity of this solution is O(n * n * MAX_WORD_LEN).
"""

"""
EFFICIENT APPROACH: O(N) SPACE COMPLEXITY: O(N)
An efficient solution is to use Hashing. We insert all votes in a hash map and keep track of counts of different names. 
print the person with maximum votes while traversing
"""

def max_vote(arr):
    dict = {}
    winner = ""
    max_vote = - sys.maxsize -1
    for i in range(len(arr)):
        if arr[i] not in dict:
            dict[arr[i]] = 1
        else:
            dict[arr[i]] += 1

        if max_vote < dict[arr[i]]:
            max_vote = dict[arr[i]]
            winner = arr[i]
        elif dict[arr[i]] == max_vote and winner > arr[i]:
            winner = arr[i]
    return winner


print(max_vote(["john","johnny","jackie","johnny","john","jackie","jamie","jamie","john","johnny","jamie","johnny","john"]))