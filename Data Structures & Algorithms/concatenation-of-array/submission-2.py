class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
      #initialize ans array
      # loop through the nums array and append every element into ans
      # outter loop will state the concatenation time
        ans = []
        for n in range(2):
            for num in nums:
                ans.append(num)
        return ans
    