class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Use a hash map to record previous result
        # hash key is the value innn the array; hash value is index of current value
        # Time Complexity: O(n), Spcae O(n)
        record = {}
        length = len(nums)

        for index in range(length):
        	if nums[index] in map:
        		return record[nums[index]], index
        	else:
        		record[target - nums[index]] = index

        # if the program chould reach here, it meanns that no such pair, 
        # return -1, -1 as an invalid answer
        return -1, -1

