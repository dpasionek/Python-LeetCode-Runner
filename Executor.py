import LongestSubstr
from Utility import TimeoutHandler

sol = LongestSubstr.Solution()

def main():
    # Create function timeout

    testCases = {
        "abcabcbb" : 3,
        "bbbbb" : 1,
        "pwwkew" : 3,
        "": 0,
        " ": 1,
        "c": 1,
        "au": 2
    }
    timeoutHandler = TimeoutHandler.TimeoutHandler(1, sol.lengthOfLongestSubstring)

    for testCase in testCases:
        try:
            res = timeoutHandler.run(testCase)
        except Exception as msg:
            print("The testcase '{0}' Timed Out!".format(testCase))
            print("Test Output:\n")
            timeoutHandler.getLog()
            continue
        
        if(res != testCases[testCase]):
            print("Test Case: {0} failed.".format(testCase))
            print("\tExpected: {0}  Got: {1}".format(testCases[testCase], res))
            print("\tTest Output:\n")
            timeoutHandler.getLog()
        else:
            print("Test Case: {0} passed!".format(testCase))


if __name__ == '__main__':
    main()