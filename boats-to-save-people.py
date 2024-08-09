class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        heavyP = len(people)-1
        lightP = 0
        people.sort()
        while heavyP >= lightP:
            if people[heavyP]+people[lightP] <= limit:
                boats += 1 
                heavyP -= 1 
                lightP += 1
            else :
                heavyP -= 1
                boats += 1 
        return boats