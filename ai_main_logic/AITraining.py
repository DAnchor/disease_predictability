from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import os
from threading import Thread
import time
"""
this class is for
AI training
"""


class AITraining(Thread):

    """
    constructor 
    """
    def __init__(self, *args):
        self.__ai_test = args
        Thread.__init__(self)


    """
    setters
    """
    # user selection
    def setXUserSelection(self, xUserSelection):
        self.__xUserSelection = xUserSelection

    # tensorflow settings
    def setSettings(self, settings):
        self.__settings = settings

    """
    getters
    """
    # user selection
    def getXUserSelection(self):
        return self.__xUserSelection
    
    # tensorflow settings
    def getSettings(self):
        return self.__settings

    # user selection method which selects one of three options
    def trainingUserSelection(self):
        while True:
            try:
                self.setXUserSelection(int(input(
                    "Please select one of the following: 1 Cancer, 2 Diabetes, 3 Heart >>> "
                )))
                if not int(self.getXUserSelection()):
                    raise ValueError(
                        "Must be a integer value, but not a {:s}".format(self.getXUserSelection())
                    )
                elif (
                        (self.getXUserSelection() != 1) and
                        (self.getXUserSelection() != 2) and
                        (self.getXUserSelection() != 3)
                ):
                    raise ValueError(
                        "Please select one of the following: 1, 2, or 3"
                    )
            except Exception as error:
                print(
                    "Raised following error:\n{:s}".format(repr(error))
                )
                continue
            else:
                break
                pass
        return self.getXUserSelection()

    # attaching path based on user selection
    def trainingSetAISettingsValuesBasedOnUserChoice(self):
        self.setSettings(list())
        if self.getXUserSelection() == 1:
            print("\nRunning >>> AI training: [CANCER] mode...")
            self.getSettings().append("/cancer.csv")
            self.getSettings().append(9)
            return self.getSettings()
        elif self.getXUserSelection() == 2:
            print("\nRunning >>> AI training: [DIABETES] mode...")
            self.getSettings().append("/diabetes.csv")
            self.getSettings().append(19)
            return self.getSettings()
        else:
            print("\nRunning >>> AI training: [HEART] mode...")
            self.getSettings().append("/heart.csv")
            self.getSettings().append(13)
            return self.getSettings()

    # thread
    def run(self):
        print(self)
        time.sleep(2)

    # main function that invokes AI
    def trainingKerasAIModelExecution(self):
        # parameters for AI
        self.__pathForCSV = os.path.dirname(os.path.abspath(__file__))
        self.__csvFileSelection = self.__settings.__getitem__(0)
        self.__listLength = int(self.__settings.__getitem__(1))
        self.__lines = sum(1 for line in open(self.__pathForCSV + self.__csvFileSelection))
        
        # declaring data-set for AI
        self.__dataSet = loadtxt(self.__pathForCSV + self.__csvFileSelection, delimiter=',')

        # split into input (X) and output (y) variables
        self.__X = self.__dataSet[:, 0:self.__listLength]
        self.__y = self.__dataSet[:, self.__listLength]

        # declare the keras model
        self.__model = Sequential()
        self.__model.add(Dense(round(self.__listLength * .5), input_dim=self.__listLength, activation='relu'))
        self.__model.add(Dense(self.__listLength, activation='relu'))
        self.__model.add(Dense(1, activation='sigmoid'))

        # compile the keras model
        self.__model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        # fit the keras model on the dataset
        self.__model.fit(self.__X, self.__y, epochs=189, batch_size=10)

        # evaluate the keras model
        _, self.__accuracy = self.__model.evaluate(self.__X, self.__y)
        self.__result = ('Prediction precision >>> %0.1f' % (self.__accuracy * 100))
        print(self.__result)

    # main method
    def __main__(self):
        self.run()
        self.trainingUserSelection()
        self.trainingSetAISettingsValuesBasedOnUserChoice()
        self.trainingKerasAIModelExecution()
