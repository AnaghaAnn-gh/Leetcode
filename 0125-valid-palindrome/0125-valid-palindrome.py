class Solution:
    def isPalindrome(self, s: str) -> bool:
      str=''
      for i in s:
        if i.isalnum() :
          str += i.lower()
      if str == str[::-1]:
        return True
      else:
        return False


        