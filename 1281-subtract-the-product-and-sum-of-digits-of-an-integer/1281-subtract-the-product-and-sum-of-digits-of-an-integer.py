class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum_of_digits = 0
        product_of_digits = 1
        while n > 0:
            digit = n % 10  
            sum_of_digits += digit  
            product_of_digits *= digit  
            n = n // 10 
        return product_of_digits-sum_of_digits