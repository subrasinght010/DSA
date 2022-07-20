class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(num):
            rob1, rob2 = 0, 0
            for n in num:
                temp=max(rob2+n,rob1)
                rob2=rob1
                rob1=temp
            return rob1
        return max(nums[0],dfs(nums[1:]),dfs(nums[:-1]))
