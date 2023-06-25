import abc


class AbstractDiagnose(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def setAge(self, age):
        pass

    @abc.abstractmethod
    def getAge(self):
        pass

    @abc.abstractmethod
    def getClassName(self):
        pass

    @abc.abstractmethod
    def stdOut(self):
        pass
