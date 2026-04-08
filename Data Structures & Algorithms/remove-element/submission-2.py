class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = r = 0
        for r in range(0, len(nums)):
            if(val != nums[r]):
                nums[l] = nums[r]
                l+=1;
        return l;





# //have 2 pointers starts from 0, 
# //loop through the array 
# //if the nums[r] !== val then nums[l] = nums[r]
# //increase l++;
# //return l