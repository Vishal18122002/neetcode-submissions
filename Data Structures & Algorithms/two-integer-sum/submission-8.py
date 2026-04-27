class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k={}
        for i in range(len(nums)):
            val=target-nums[i]
            if val in k and k[val]!=i:
                return [k[val],i]
            else:
                k[nums[i]]=i
        
        


        