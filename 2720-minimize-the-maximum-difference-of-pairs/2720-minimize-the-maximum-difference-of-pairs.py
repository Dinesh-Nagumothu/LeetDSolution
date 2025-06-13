class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p==0:
            return 0
        n = len(nums)
        nums.sort()
        if p<<1==n:
            imax = 0
            for i in range(0, n-2+1, 2):
                imax = max(imax, nums[i+1]-nums[i])
            return imax
        que = [nums[i]-nums[i-1] for i in range(1, n)]
        def check(dmax):
            i = 0
            cnt = 0
            while i<len(que) and cnt<p:
                if que[i]<=dmax:
                    i += 2
                    cnt += 1
                else:
                    i += 1
            return cnt>=p
        l, r = 0, max(que)
        while l<r:
            m = (l+r)>>1
            if not check(m):
                l = m + 1
            else:
                r = m
        return l
