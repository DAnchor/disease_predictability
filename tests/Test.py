from ai_main_logic.AIPredict import AIPredict
from ai_main_logic.AITraining import AITraining
from factory.ClassFactory import ClassFactory
import time
from threading import Thread
"""
testing ai classes
"""


class Test(Thread):

    def __init__(self, *args):
        self.main = args
        Thread.__init__(self)

    # query test cancer
    def queryTest(self):
        """
        :return:
        """
        self.xClass = ClassFactory.createClass("Cancer")
        self.xClass.setAge(51)
        self.xClass.setBMI(10)
        self.xClass.setGlucose(60)
        self.xClass.setInsulin(2)
        self.xClass.setHOMA(1)
        self.xClass.setLeptin(10)
        self.xClass.setAdiponectin(15)
        self.xClass.setResistin(6)
        self.xClass.setMCP1(543)
        self.xClass.setClassification(1)

        # query write to CSV test file
        self.xClass.passQueryToCSV()

        # stdout
        self.xClass.stdOut()

    # ai predict test
    def aiPrediction(self):
        self.xAiRun = AIPredict()
        self.xAiRun.__main__()

    # ai training
    def aiTraining(self):
        self.xAiRun = AITraining()
        self.xAiRun.__main__()
        time.sleep(3)

    # initialise methods
    def selection(self):
        while True:
            try:
                self.userChoice = int(
                    input(
                        "Mode selection: 1 query test, 2 training mode, 3 predict mode, type or 4 for exit >>> "
                    )
                )
                if not int(self.userChoice):
                    raise ValueError()
                elif (self.userChoice < 1) and (self.userChoice > 4):
                    raise ValueError()
            except Exception as error:
                print('Raised error:\n%s' % (repr(error)))
                continue
            else:
                break
                pass
        return self.userChoice

    # triggering selection based on user choice
    def triggerSelection(self, userChoice):
        if self.userChoice == 1:
            print("\nMode selected >>> QUERY TEST!")
            self.queryTest()
        elif userChoice == 2:
            print("\nMode selected >>> AI TRAINING!")
            self.aiTraining()
        elif userChoice == 3:
            print("\nMode selected >>> AI PREDICTION")
            self.aiPrediction()
        elif userChoice == 4:
            print("\nEXITING SYSTEM...")
            exit(0)
        else:
            print("ERROR selection:\nsomething went wrong, try again later...")

    def run(self):
        print(self)

    # main method
    def __main__(self):
        self.run()
        self.triggerSelection(self.selection())


Test().__main__()
# xRun.__main__()
