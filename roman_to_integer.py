class Solution:
    def romanToInt(s):
        d = {
            'I' : 1, 
            'V' : 5, 
            'X' : 10, 
            'L' : 50,
            'C' : 100, 
            'D' : 500, 
            'M' : 1000
        }
        
        arr = []
        now = s[0]
        count = 0
        for i in range(len(s)):
            if s[i] == now:
                count += 1
                if i == len(s) - 1:
                    arr.append(d[now] * count)
                    # print(arr)
            else:
                arr.append(d[now] * count)
                count = 1
                now = s[i]
                # print(arr)
                if i == len(s) - 1:
                    arr.append(d[now] * count)
                    # print(arr)
        # print(arr)     
        res = []
        k = 0
        while k <= len(arr) - 2:

            if arr[k] <= arr[k + 1]:
                res.append(arr[k + 1] - arr[k])
                k += 2
            else:
                res.append(arr[k])
                k += 1
        if k == len(arr) -1:
            res.append(arr[k])

        # print(res)
        return sum(res)

s = "MMMCMXCIX"

print(Solution.romanToInt(s))               