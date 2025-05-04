class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            # 짝수 번째 값의 계산
            if i % 2 == 0:
                sum += n

        return sum
