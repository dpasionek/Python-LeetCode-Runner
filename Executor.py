import LongestSubstr
import time
from Utility import TimeoutHandler

sol = LongestSubstr.Solution()

def main():
    # Create function timeout
    f = open("test.txt", 'r')
    testCases = {
        "abcabcbb" : 3,
        "bbbbb" : 1,
        "pwwkew" : 3,
        "": 0,
        " ": 1,
        "c": 1,
        "au": 2,
        "aA":2,
        "ohomm": 3,
        "rggtlnpgkqksefchmdaqyhdnatpwbtytbho":11,
        "crdghfrgrgyanjclxgzuomlqxfgeqguuaxdjcuruapwpbzbyhau": 12,
        #f.read():95
    }
    f.close()
    timeoutHandler = TimeoutHandler.TimeoutHandler(20, sol.lengthOfLongestSubstring)

    for testCase in testCases:
        now = time.time()
        try:
            res = timeoutHandler.run(testCase)
            end = time.time()
        except Exception as msg:
            end = time.time()
            print("The testcase '{0}' Timed Out!\n\tExecution time {1}s".format(testCase, (end-now)))
            print("Test Output:\n")
            timeoutHandler.getLog()
            print()
            continue
        
        if(res != testCases[testCase]):
            print("Test Case: {0} failed.\n\tExecution time {1}s".format(testCase, (end-now)))
            print("\tExpected: {0}  Got: {1}".format(testCases[testCase], res))
            print("\tTest Output:\n")
            timeoutHandler.getLog()
            print()
        else:
            print("Test Case: {0} passed!\n\tExecution time {1}s".format(testCase, (end-now)))
            print()


if __name__ == '__main__':
    main()