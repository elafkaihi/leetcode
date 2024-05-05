class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else : 
                dict[i] = 1
        # find the element with max count
        majority = max(dict.values())
        for key, value in dict.items() : 
            if value == majority:
                return key
