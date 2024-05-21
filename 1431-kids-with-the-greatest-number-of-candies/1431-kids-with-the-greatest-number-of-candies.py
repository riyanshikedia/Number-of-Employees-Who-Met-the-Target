class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxcand=max(candies)
        result=[]
        for i in range(len(candies)):
            a=candies[i]+extraCandies
            result.append(a>=maxcand)
        return result
        