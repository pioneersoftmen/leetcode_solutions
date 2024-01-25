class Solution:
    def index_finder(index, array):
        for i in range(len(array)):
            if array[i] >= index:
              return i
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        new_nums = [index + char for index, char in enumerate(nums)]
        count = 0
        index = len(new_nums) - 1
        while index != 0:
            count += 1
            index = Solution.index_finder(index, new_nums[:index + 1])
        return count 
