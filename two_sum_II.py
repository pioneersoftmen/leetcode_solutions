class Solution:
    def binary_search(self, arr, low, high, target):
        while low <= high:
            mid = (high + low) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] > target:
                high = mid - 1
            else: 
                low = mid + 1
        return None
        
        
    def twoSum(self, numbers, target: int):
        if len(numbers) == 2:
            return [0, 1]
        for j in range(len(numbers) - 1):
            
            wanted = target - numbers[j]
            is_there = self.binary_search(numbers[j + 1:], 0, len(numbers[j + 1:]) - 1, wanted)
            if is_there is not None:
                return [j + 1, is_there + j + 2]
    
numbers = [-1,0]
target = -1
a = Solution()

print(a.twoSum(numbers, target))