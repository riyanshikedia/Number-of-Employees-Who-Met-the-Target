class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        count=0
        for x in hours:
            if x>=target:
                count+=1
        return count
        
