class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        m = n - numFriends + 1
        result = ""
        if numFriends == 1:
            return word
        
        for i in range(n):
            result = max(word[i:i + m], result)
            
        return result        