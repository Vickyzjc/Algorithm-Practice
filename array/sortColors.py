class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if (nums is None) or (len(nums) == 0):
        	return

        length = len(nums)
        i = 0
        j = 0
        k = length - 1

        while j <= k:
            if nums[j] == 2:
                self.swap(nums, j, k)
                k = k - 1
            elif nums[j] == 0:
                self.swap(nums, i, j)
                i = i + 1
                j = j + 1
            else:
        		j = j + 1
                
    def swap(self, nums, left, right):
    	temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp

