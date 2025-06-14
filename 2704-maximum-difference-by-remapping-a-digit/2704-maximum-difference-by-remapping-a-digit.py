class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        # Make max: replace first digit that's not 9 with 9
        for d in s:
            if d != '9':
                max_num = s.replace(d, '9')
                break
        else:
            max_num = s

        # Make min: replace first digit that's not 0 with 0
        for d in s:
            if d != '0':
                min_num = s.replace(d, '0')
                break
        else:
            min_num = s

        return int(max_num) - int(min_num)
