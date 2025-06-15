class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        
        # Maximize: Replace first non-9 digit with 9
        for digit in s:
            if digit != '9':
                max_version = s.replace(digit, '9')
                break
        else:
            max_version = s  # Already all 9s

        # Minimize: Replace first digit != 1 with 1 if it's the first digit,
        # else replace any non-0 digit with 0
        if s[0] != '1':
            min_version = s.replace(s[0], '1')
        else:
            for digit in s[1:]:
                if digit != '0' and digit != s[0]:
                    min_version = s.replace(digit, '0')
                    break
            else:
                min_version = s  # Already minimal

        return int(max_version) - int(min_version)
