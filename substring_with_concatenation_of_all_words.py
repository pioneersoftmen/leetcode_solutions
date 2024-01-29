class Solution:
    def findSubstring(self, s, words):
        d = {}
        n = len(words)
        word_length = len(words[0])
        for i in range(n):
            if words[i] in d:
                d[words[i]] += 1
            else:
                d[words[i]] = 1
        res = []
        window_length = word_length * n
        for j in range(len(s) - window_length + 1):
            win_hash = {}
            k = j
            while k < j + window_length:
                if s[k:k+word_length] in win_hash:
                    win_hash[s[k:k + word_length]] += 1
                    k += word_length
                else:
                    win_hash[s[k:k + word_length]] = 1
                    k += word_length
            if win_hash == d:
                res.append(j)

        return res



s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
a = Solution()
print(a.findSubstring(s, words))