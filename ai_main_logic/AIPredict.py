from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import os


class AIPredict:
    """
    constructor overload
    """
    def __init__(self, *args):
        self.ai_predict = args

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
    def predictingUserSelection(self):
        while True:
            try:
                self.setXUserSelection(int(input(
                    "Please select one of the following: 1 Cancer, 2 Diabetes, 3 Heart: "
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
    def predictingSetAISettingsValuesBasedOnUserChoice(self):
        self.setSettings(list())
        if self.getXUserSelection() == 1:
            print("\nDiagnosing >>> Cancer possible precautions...")
            self.getSettings().append("/cancer.csv")
            self.getSettings().append(9)
            return self.getSettings()
        elif self.getXUserSelection() == 2:
            print("\nDiagnosing >>> Diabetes possible precautions...")
            self.getSettings().append("/diabetes.csv")
            self.getSettings().append(19)
            return self.getSettings()
        else:
            print("\nDiagnosing >>> Heart possible precautions...")
            self.getSettings().append("/heart.csv")
            self.getSettings().append(13)
            return self.getSettings()

    # main function that invokes AI
    def predictingKerasAIModelExecution(self):
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
        self.__model.fit(self.__X, self.__y, epochs=189, batch_size=10, verbose=0)

        # make class predictions with the model
        self.__predictions = self.__model.predict_step(self.__X)

        # summarize
        for i in range(self.__lines):
            self.__simulation = (
                    '%s >>> (predicted value) %d >>> (static value %d)' %
                    (
                        self.__X[i].tolist(), self.__predictions[i], self.__y[i]
                    )
            )
            print(self.__simulation)

    # main method
    def __main__(self):
        self.predictingUserSelection()
        self.predictingSetAISettingsValuesBasedOnUserChoice()
        self.predictingKerasAIModelExecution()


