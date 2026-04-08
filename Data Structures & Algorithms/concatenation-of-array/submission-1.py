class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #create ans array length of 2xnums
        #push elements from nums into ans 2x

        ans = [] * 2 * len(nums)

        for i in range (2):
             for n in range(0, len(nums)):
                ans.append(nums[n])

           
            
        return ans