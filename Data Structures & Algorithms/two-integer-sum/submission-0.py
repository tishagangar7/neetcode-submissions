class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference=0
        ans=[]
        for i in range(len(nums)-1):
            difference=target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==difference:
                    ans.append(i)
                    ans.append(j)

        return ans