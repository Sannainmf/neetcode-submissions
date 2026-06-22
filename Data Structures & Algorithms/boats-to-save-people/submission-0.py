class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        

        people = sorted(people)

        l = 0
        r = len(people) - 1
        count = 0

        while l <= r:
            sum = people[l] + people[r]
            if sum > limit:
                count += 1
                r -= 1
            elif sum <= limit:
                count += 1
                l += 1
                r -= 1

        return count

    



            


        