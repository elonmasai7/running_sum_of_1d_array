class Solution(object):
    def runningSum(self, nums):
        running_sum = []
        current_sum = 0
        for num in nums:
            current_sum += num
            running_sum.append(current_sum)
        return running_sum


solution = Solution()

nums1 = [1, 2, 3, 4]
nums2 = [1, 1, 1, 1, 1]
nums3 = [3, 1, 2, 10, 1]

print(solution.runningSum(nums1))
print(solution.runningSum(nums2))
print(solution.runningSum(nums3))
