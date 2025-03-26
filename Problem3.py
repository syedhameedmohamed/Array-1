# // Time Complexity : O(m*n)
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode : Yes
# // Three line explanation of solution in plain english

# // Your code here along with comments explaining your approach

# Set up boundaries between the top and bottom row and left and right columns
# While the boundaries don't exceed, first traverse from left to right across the top row. Then once we reach the right boundary, move from top to bottom along the right column
# then once we reach the bottom row, move from right to left along the bottom row, then once we reach the left column, move from bottom to top across the left column
# While traveling through each row or column, store the respective values in a result matrix and return the result

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        top, left = 0, 0
        bottom, right = m - 1, n - 1
        
        result = []

        while top <= bottom and left <= right:
            # Traverse from left to right, along top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Traverse from top to bottom, along right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Traverse from right to left, along bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            # Traverse from bottom to top, along left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result

            
