class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        product_without_zero = 1
        number_of_zeros = 0
        for i in nums:
            if i == 0:
                number_of_zeros += 1
            else:
                product_without_zero = product_without_zero * i


        output_array = []

        if (number_of_zeros > 0):
            if (number_of_zeros == 1):
                for i in nums:
                    if i == 0:
                        output_array.append(product_without_zero)
                    else:
                        output_array.append(0)
            else:
                for i in nums:
                    output_array.append(0)
        else:
            for i in nums:
                output_array.append(product_without_zero//i)


        return output_array





# print(Solution().productExceptSelf(nums = [1,2,3,4]))