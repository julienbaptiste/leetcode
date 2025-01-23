class Solution(object):
    def twoSum(self, nums, target):
        numbers_set = set(nums) # set of numbers

        # Looping on numbers
        for n in nums:
            # if the difference is in the list, we have our solutions
            if (target - n) in numbers_set:
                # just need to get the indexes
                # caution if a number is half of the target
                if ((target - n) != n):
                    return [nums.index(n), nums.index(target - n)]

                # in case the number is half of the target
                # we must ensure it is twice in the list
                if (nums.count(n) == 2):
                    return [i for i in range(len(nums)) if nums[i]==n]
            