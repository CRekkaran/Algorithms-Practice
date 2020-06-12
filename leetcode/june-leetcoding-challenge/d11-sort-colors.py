class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        le = [0,0,0]
        for i in range(n):
            le[nums[i]] += 1
        for i in range(le[0]):
            nums[i] = 0
        for i in range(le[1]):
            nums[i+le[0]] = 1
        for i in range(le[2]):
            nums[i+le[0]+le[1]] = 2
        
