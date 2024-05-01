class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        i = 0 
        j = 1 
        count = 1
        while j < len(nums):
            if nums[i] == nums[j] :
                if count < 2 :
                    i += 1 
                    nums[i] = nums[j]
                    j += 1
                    count += 1    
                else :
                    j += 1
            elif nums[i] < nums[j] :
                i += 1
                nums[i] = nums[j]
                j += 1
                count = 1

        return i+1
        
