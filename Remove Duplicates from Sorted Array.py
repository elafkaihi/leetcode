class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        i = 0
        j = 0
        k = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j = j+1
            elif nums[i] < nums[j]:
                nums[i+1] = nums[j]
                i += 1
                j += 1
                k += 1 
        return k     
