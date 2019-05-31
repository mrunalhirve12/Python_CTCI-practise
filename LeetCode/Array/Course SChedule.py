"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""
from pip._vendor.msgpack.fallback import xrange


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {}
        in_degrees = {}

        for i in xrange(numCourses):
            graph[i] = []
            in_degrees[i] = 0
        for c, p in prerequisites:
            graph[p].append(c)
            in_degrees[c] += 1

        # do a bfs/topological sort to cover all courses
        curr_courses = [i for i in xrange(numCourses) if in_degrees[i] == 0]
        courses_taken = 0
        while curr_courses:
            curr_course = curr_courses.pop(0)
            courses_taken += 1
            for next_course in graph[curr_course]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:
                    curr_courses.append(next_course)

        return courses_taken == numCourses



s = Solution()
s.canFinish(3, [[1,0],[2,1]])
