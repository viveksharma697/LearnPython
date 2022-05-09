# find the largest rectangle in histogram
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [0] * n
        right = [0] * n
        stack = []
        #getting the left elements
        for i in range(n):
            if not stack:
                left[i] = 0
            else:
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                left[i] = stack[-1]+1 if stack else 0
            stack.append(i)
        stack.clear()
        #getting the right elements
        for i in range(n-1,-1,-1):
            if not stack:
                right[i] = n-1
            else:
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                right[i] = stack[-1]-1 if stack else n-1
            stack.append(i)

        #calculating the area
        max_area = 0
        for i in range(n):
            height = heights[i]
            width = right[i]-left[i]+1
            area = height * width
            if area > max_area:
                max_area = area
        return max_area