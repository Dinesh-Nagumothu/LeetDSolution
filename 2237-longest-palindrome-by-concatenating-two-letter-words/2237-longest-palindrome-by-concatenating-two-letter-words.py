class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        center_used = False

        for word in list(count.keys()):
            rev = word[::-1]
            if word == rev:
                # Use as many pairs as possible (e.g., "aa", "bb")
                pairs = count[word] // 2
                length += pairs * 4
                count[word] -= pairs * 2
            elif rev in count:
                # Use min of both word and its reverse
                pairs = min(count[word], count[rev])
                length += pairs * 4
                count[word] -= pairs
                count[rev] -= pairs

        # Try placing one remaining symmetric word like "aa" in the center
        if not center_used:
            for word in count:
                if word[0] == word[1] and count[word] > 0:
                    length += 2
                    break

        return length
