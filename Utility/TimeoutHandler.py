
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
        self.log_size = lambda: len(self.last_logs)

    def getLog(self, printToFile):
        print_thread = threading.Thread(target=self.doPrint(printToFile))
        print_thread.start()
        print_thread.join()

    def doPrint(self, printToFile):
        end = time.time() + (30 * 1000)
        sys.__stdout__.write("Attempting print in {0}s".format(end * 1000))
        if(printToFile):
            file = open("./log-{0}.txt" + time.localtime())
            try:
                for l in self.last_logs:
                    if(time.time() >= end):
                        break
                    file.write(l)
            except Exception:
                sys.__stdout__.write("Error writing to file!")
            finally:
                file.close()
        else:
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
        
        

