class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(num: int) -> bool:
            s = str(num)
            if len(s) % 2 != 0:
                return False
            mid = len(s) // 2
            left_sum = sum(int(d) for d in s[:mid])
            right_sum = sum(int(d) for d in s[mid:])
            return left_sum == right_sum

        count = 0
        for num in range(low, high + 1):
            if is_symmetric(num):
                count += 1
        return count
