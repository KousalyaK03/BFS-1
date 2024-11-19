# Approach:
# 1. Represent the course prerequisites as a directed graph using an adjacency list.
# 2. Perform a topological sort using Kahn's algorithm (BFS) to detect cycles.
# 3. If all courses are processed (no cycle detected), return True; otherwise, return False.


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the adjacency list and in-degree count
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses

        for course, pre in prerequisites:
            adj_list[pre].append(course)
            in_degree[course] += 1

        # Initialize a queue with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # Count of courses that can be processed
        processed_courses = 0

        while queue:
            course = queue.popleft()
            processed_courses += 1

            # Reduce the in-degree of dependent courses
            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1
                # If in-degree becomes 0, add it to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If all courses are processed, return True; otherwise, there's a cycle
        return processed_courses == numCourses

# Time Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.
# Space Complexity: O(V + E) for the adjacency list and in-degree array.
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No
