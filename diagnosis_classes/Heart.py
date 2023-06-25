from diagnosis_classes.AbstractDiagnose import AbstractDiagnose
import sys
sys.path.append("..")


class Heart(AbstractDiagnose):

    """
    constructor overloading
    """
    # cancer constructor
    def __init__(self, *args):
        self.__cancer = args
        self.__name = "Heart"

    """
    setters
    """
    # age
    def setAge(self, age):
        __age = age

    """
    getters
    """
    # age
    def getAge(self):
        self.__age

    # get class name
    def getClassName(self):
        return self.__name

    """
    to string method
    """
    # stdout
    def stdOut(self):
        print("%" % (
            self.getAge()
        )
        )

