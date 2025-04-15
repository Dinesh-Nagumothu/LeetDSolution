from typing import List

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 2)  # 1-based indexing

    def update(self, i, delta):
        i += 1  # convert to 1-based
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2 = {num: i for i, num in enumerate(nums2)}
        mapped = [pos2[num] for num in nums1]

        left_tree = FenwickTree(n)
        left_counts = [0] * n

        for i in range(n):
            left_counts[i] = left_tree.query(mapped[i] - 1)
            left_tree.update(mapped[i], 1)

        right_tree = FenwickTree(n)
        right_counts = [0] * n

        for i in range(n - 1, -1, -1):
            right_counts[i] = right_tree.query(n - 1) - right_tree.query(mapped[i])
            right_tree.update(mapped[i], 1)

        result = 0
        for i in range(n):
            result += left_counts[i] * right_counts[i]

        return result
