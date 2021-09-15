class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace("\\\\", "\\").replace("\\\"", '"')

        if(s == ''):
           return 0
        if(s.isspace() or len(s) == 1):
            return 1
        if(len(s) > 500):
            sPrime = ''.join(s[:500])
            firstLetter = s[0]
            idx = [n for n in range(len(sPrime)) if s.find(firstLetter, n) == n]
            diff_list = []
            for item_1, item_2 in zip(idx[0::], idx[1::]):
                diff_list.append(item_2 - item_1)
            if(len(set(diff_list)) == 1):
                s = ''.join(sPrime[idx[0]:idx[1]])
                print("Updated String: {0}".format(s))
                
           
        return len(self.getLargestSubstr(s))
        
    def getLargestSubstr(self, s):
        ptr_start = 0
        ptr_end = len(s)
        largestSubStr = ""
        sList = [char for char in s]
        print("Original String: {0} (Length {1})".format(s if len(s) < 50 else s[:50] + "...", len(s)))
        while(ptr_start < (len(sList))):
            if((ptr_end - ptr_start) >= len(largestSubStr)):
                substring = sList[ptr_start:ptr_end]
                print("Current Substring [{0}-{1}]: {2}".format(ptr_start, ptr_end,substring))
                if(self.isSubstringOk(s, substring)):
                    if(largestSubStr is None):
                        largestSubStr = substring
                    elif(substring != largestSubStr and len(largestSubStr) < len(substring)):
                        print("Setting largest SubStr: {0}".format(''.join(substring)))
                        largestSubStr = substring
                    else:
                        print("Substring already counted!")
                else:
                    print("Not a valid substring: {0}".format(substring))
            if(ptr_end == ptr_start):
                ptr_start = ptr_start + 1
                ptr_end = len(s)
                print("Incrementing ptr_start: {0}\n\n".format(ptr_start))
            else:
                ptr_end = ptr_end - 1
                print("Incrementing ptr_end: {0}\n\n".format(ptr_end))
        print("Ending search. Longest substring found: {0} with length {1}".format(largestSubStr, len(largestSubStr))) 
        return largestSubStr           

    def isSubstringOk(self, string, substring):
        substring = ''.join(substring)
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