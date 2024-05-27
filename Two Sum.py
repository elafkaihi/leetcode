class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti = {}
        for i in range(len(nums)) : 
            diff = target - nums[i]
            if diff in dicti :
                return [dicti[diff],i]
            else : 
                dicti[nums[i]] = i
