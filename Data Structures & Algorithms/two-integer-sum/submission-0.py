class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap
        # loop through the nums array and keep track of number and its index
        # check if the diff is in the hashmap 
        # return the index of the number in the hashmap and the index of the number from the nums array that sum target
        # if the diff is not in the hasmap => add the number and its index into the hashmap

        prevMap = {} #val: index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return