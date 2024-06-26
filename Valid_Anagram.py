class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dicti = {}
        #make dictionary of the first 
        for let in s : 
            if let in dicti : 
                dicti[let] += 1 
            else :
                dicti[let] = 1
        
        for let in t : 
            if let not in dicti or dicti[let] == 0 : 
                return False
            else : 
                dicti[let] -= 1 
        
        for key, value in dicti.items() :
            if value != 0:
                return False 
            else: 
                return True 