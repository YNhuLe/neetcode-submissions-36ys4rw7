class Solution:
   
        # given string s
        # return True if it's palindrome( string that read same way forward and backward)
        # return False if not
        # only check on the alphanumeric

        #SOLUTION 1
            # create a new empty string, loop through the s
            #check every character if it is alphanumeric
            # if yes => turn them to lowercase, add into the new string
            # return True if the newStr is the same as the reversed of its
        #   def isPalindrome(self, s: str) -> bool:
        #         newStr = ''
        #         for c in s:
        #             if c.isalnum():
        #                 newStr += c.lower()
        #         return newStr == newStr[::-1]
                
        #SOLUTION 2:
            #have 2 pointers left from the start, right from the end of the string
            # while l, r have not left and if the pointer the left pointing on non-alphanumeric the pointer left inceament
            # same for pointer r
            # if charater at the pointer left not same as character at the pointer right, return False
            # keep pointer left increament, pointer right decreament
            # return True when2 pointer meet
        
    def isPalindrome(self, s: str) -> bool:           
        l, r = 0, len(s) -1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l +=1
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l, r = l +1, r-1
        return True
#check if the character is alphanumeric
    def alphaNum(self, c):
        return ( ord('A') <= ord(c) <= ord('Z') or 
         ord('a') <= ord(c) <= ord('z') or 
          ord('0') <= ord(c) <= ord('9'))