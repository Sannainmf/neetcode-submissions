class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        """
        people i is the wweight of the ith person
        each boat carries at most 2 people
        weight of the boat is at most limit
        """

        people = sorted(people)
        
        l = 0
        r = len(people) - 1
        count = 0

        while l <= r:
            s = people[l] + people[r]
            if s > limit:
                r -= 1
                count += 1
            else:
                l += 1
                r -= 1
                count += 1

        return count

        
