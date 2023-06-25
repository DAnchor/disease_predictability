import time
from threading import Thread


class MultiThreading(Thread):

    def __init__(self, *args):
        self.__t = args
        Thread.__init__(self)

    def getThread(self):
        return self.__t

    def run(self):
        print(self.__t)


x = MultiThreading()
x.run()
