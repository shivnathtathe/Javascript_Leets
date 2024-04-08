from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stack = deque(sandwiches[::-1])
        queue = deque(students)
        iterations = 0
        
        while queue:
            if queue[0] == stack[-1]:
                queue.popleft()
                stack.pop()
                iterations = 0  # Reset iterations counter
            else:
                queue.append(queue.popleft())
                iterations += 1
                
            if iterations == len(queue):  # If all students have gone through without taking a sandwich
                return len(queue)
                
        return 0
