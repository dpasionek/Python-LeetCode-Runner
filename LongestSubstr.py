class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(s == ''):
           return 0
        if(s.isspace() or len(s) == 1):
            return 1
        return len(self.getLargestSubstr(s))
        

    def getLargestSubstr(self, s):
        ptr_start = 0
        ptr_end = 0
        largestSubStr = ""
        print("Original String: {0} (Length {1})".format(s, len(s)))
        while(ptr_start <= (len(s))):
            substring = s[ptr_start:ptr_end]
            print("Current Substring [{0}-{1}]: {2}".format(ptr_start, ptr_end,substring))
            if(self.isSubstringOk(s, substring)):
                if(largestSubStr is None):
                    largestSubStr = substring
                elif(substring != largestSubStr and len(largestSubStr) < len(substring)):
                    print("Setting largest SubStr: {0}".format(substring))
                    largestSubStr = substring
                else:
                    print("Substring {0} already counted!".format(substring))
            else:
                print("Not a valid substring: {0}".format(substring))
            if(ptr_end == (len(s) - 1)):
                ptr_start = ptr_start + 1
                print("Incrimenting ptr_start: {0}".format(ptr_start))
            else:
                ptr_end = ptr_end + 1
                print("Incrimenting ptr_end: {0}".format(ptr_end)) 
        return largestSubStr           

    def isSubstringOk(self, string, substring):
        print("Checking if substring: {0} in string {1} is okay...".format(substring, string))
        if(string.isspace() or substring.isspace()):
            return True
        if(substring == None or substring == ""):
            print("Substring is null or empty")
            return False
        if(substring not in string):
            print("Substring is not continuous in string")
            return False
        for letter in substring:
            if(substring.count(letter) > 1):
                print("Substring contains repeating letter: {0}".format(letter))
                return False
        return True