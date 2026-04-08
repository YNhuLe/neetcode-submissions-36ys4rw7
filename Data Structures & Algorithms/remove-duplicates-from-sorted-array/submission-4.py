# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         left = 1
#         for right in range(1, len(nums)):
#             if nums[right] != nums[right - 1]:
#                 nums[left] = nums[right]
#                 left +=1
#         return left
       

class Solution:
    def removeDuplicates(self, nums: List[int])-> int:
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)