class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        from collections import Counter
        cnt=Counter(words)
        res=0
        center=False
        for w in list(cnt.keys()):
        	rev=w[::-1]
        	if w==rev:
        		res+=(cnt[w]//2)*2
        		if cnt[w]%2:
        			center=True
        	elif w<rev:
        		res+=2*min(cnt[w],cnt[rev])
        return (res+(1 if center else 0))*2