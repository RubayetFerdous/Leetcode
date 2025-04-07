class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumi=sum(nums[:k])
        maxi=sumi
        for i in range(k,len(nums)):
            sumi+=nums[i]-nums[i-k]
            maxi=max(sumi,maxi)
        return round(maxi/k,5)
            
