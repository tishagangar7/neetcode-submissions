class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        #[0:5,1:6,2:7] n=3
        #ans=[0:5,1:6,2:7,3+0:5,3+1:6,3+2:,6]
        for i in range(2*len(nums)):
            if i<len(nums):
                ind=i
                ans.append(nums[ind])
            else:
                ans.append(nums[i-len(nums)])
        return ans