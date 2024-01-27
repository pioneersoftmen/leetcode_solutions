class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        for i in range(len(t)):
            try:
                if t[i] == s[si]:
                    si += 1
            except:
                break
        if si > len(s) - 1:
            return True
        return False


s = "axc"
t = "ahbgdc"
a = Solution()
print(a.isSubsequence(s, t))