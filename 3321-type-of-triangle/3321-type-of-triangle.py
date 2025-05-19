class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)
        # Check for triangle validity
        if a + b <= c:
            return "none"
        # Determine the type of triangle
        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"
