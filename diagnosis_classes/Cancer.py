from diagnosis_classes.AbstractDiagnose import AbstractDiagnose
import os


# noinspection SpellCheckingInspection
class Cancer(AbstractDiagnose):

    """
    constructor overloading
    """
    # cancer constructor
    def __init__(self, *args):
        self.__cancer = args
        self.__name = "Cancer"

    """
    setters
    """
    # age
    def setAge(self, age):
        self.__age = age

    # BMI
    def setBMI(self, bmi):
        self.__bmi = bmi

    # glucose
    def setGlucose(self, glucose):
        self.__glucose = glucose

    # insulin
    def setInsulin(self, insulin):
        self.__insulin = insulin

    # homa
    def setHOMA(self, homa):
        self.__homa = homa

    # leptin
    def setLeptin(self, leptin):
        self.__leptin = leptin

    # adiponectin
    def setAdiponectin(self, adiponectin):
        self.__adiponectin = adiponectin

    # resistin
    def setResistin(self, resistin):
        self.__resistin = resistin

    # MPC.1
    def setMCP1(self, mcp1):
        self.__mcp1 = mcp1

    # classification
    def setClassification(self, classification):
        self.__classification = classification

    """
    getters
    """
    # age
    def getAge(self):
        return self.__age

    # BMI
    def getBMI(self):
        return self.__bmi

    # glucose
    def getGlucose(self):
        return self.__glucose

    # insulin
    def getInsulin(self):
        return self.__insulin

    # homa
    def getHOMA(self):
        return self.__homa

    # leptin
    def getLeptin(self):
        return self.__leptin

    # adiponectin
    def getAdiponectin(self):
        return self.__adiponectin

    # resistin
    def getResistin(self):
        return self.__resistin

    # MCP.1
    def getMCP1(self):
        return self.__mcp1

    # classification
    def getClassification(self):
        return self.__classification

    # get class name
    def getClassName(self):
        return self.__name

    """
    pass db query into csv file
    """
    def passQueryToCSV(self):
        pathForCSV = os.path.dirname(os.path.abspath(__file__))
        result = "{:s},{:s},{:s},{:s},{:s},{:s},{:s},{:s},{:s},{:s}\n".format(
            str(self.getAge()), str(self.getBMI()),
            str(self.getGlucose()), str(self.getInsulin()),
            str(self.getHOMA()), str(self.getLeptin()),
            str(self.getAdiponectin()), str(self.getResistin()),
            str(self.getMCP1()), str(self.getClassification())
        )

        # print(pathForCSV)
        with open(pathForCSV+"/test.csv", "a") as file:
            file.write(result)
            file.close()

    """
    to string method
    """
    # stdout
    def stdOut(self):
        print(
            'age: %d, bmi: %d, glucose: %d, '
            'insulin: %d, homa: %d, leptin: %d, '
            'adiponectin: %d, resistin: %d, '
            'mcp1: %d, classification: %d' % (
                self.getAge(),
                self.getBMI(),
                self.getGlucose(),
                self.getInsulin(),
                self.getHOMA(),
                self.getLeptin(),
                self.getAdiponectin(),
                self.getResistin(),
                self.getMCP1(),
                self.getClassification()
            )
        )
