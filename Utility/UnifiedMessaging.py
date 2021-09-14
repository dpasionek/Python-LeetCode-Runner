from Utility import Singleton
import sys, inspect

class UnifiedMessaging:
    __metaclass__ = Singleton.Singleton
    def __init__(self):
        self._hidden_end = 0
        self.output = []

    def write(self, message):
        stack = inspect.stack()
        theMethod = stack[1][0].f_code.co_name
        if(not self._hidden_end and message != ""):
            self.output.append("[{0}()] {1}".format(theMethod,message))
        self._hidden_end ^= 1
        
    def getOutput(self):
        copy = self.output
        self.flush()
        return copy

    def flush(self):
        self.output = []