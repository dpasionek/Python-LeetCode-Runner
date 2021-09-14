
from Utility import UnifiedMessaging
import time
import threading
import sys


class TimeoutHandler():
    def __init__(self, timeout, function):
        self.timeout = timeout
        self.function = function
        self.result = None
        self.last_logs = []

    def getLog(self):
        if(len(self.last_logs) > 50):
            self.last_logs = []
            print("WARNING: This output is too long to display!")
            return
        for l in self.last_logs:
            print(l)

    def getStdOut(self):
        return sys.stdout.getOutput()

    def run(self, *params):

        now = time.time()
        end = now + (self.timeout * 1000)

        thread = threading.Thread(target=self.__execute__, args=params)
        thread.start()
        thread.join(timeout=self.timeout)

        if(self.result is None and end >= now):
            self.last_logs = self.getStdOut()
            sys.stdout = sys.__stdout__
            raise TimeoutError("Timed out!")

        self.last_logs = self.getStdOut()
        sys.stdout = sys.__stdout__
        return self.result    

    def __execute__(self, *args):
        sys.stdout = UnifiedMessaging.UnifiedMessaging()
        try:
            self.result = self.function(*args)
        finally:
            return self.result
        
        

