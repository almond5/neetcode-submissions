class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = sorted(s)
        sortedt =sorted(t)
        return sortedS == sortedt
        