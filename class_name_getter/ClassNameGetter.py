"""
class that will check
for current class names
e.g. (Cancer, Diabetes, Heart)
"""

class ClassNameGetter(object):

    """
    constructor overload
    """
    # constructor for class name checker
    def __init__(self, *args):
        self.__checker = args
        self.__name = ""

    """
    getter
    """
    # name
    def getClassName(self):
        return self.__name

