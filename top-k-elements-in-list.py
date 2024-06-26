from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 0
            dictionary[num] += 1
        
        # Sort the dictionary by values in descending order and get the keys
        sorted_dict = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)

        # Extract the top k keys
        top_k = [item[0] for item in sorted_dict[:k]]
        
        return top_k
