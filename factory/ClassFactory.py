from diagnosis_classes.Cancer import Cancer
from diagnosis_classes.Diabetes import Diabetes
from diagnosis_classes.Heart import Heart


class ClassFactory:
    @staticmethod
    def createClass(args):
        if "Cancer".capitalize() == args:
            return Cancer()
        elif "Diabetes".capitalize() == args:
            return Diabetes()
        elif "Heart".capitalize() == args:
            return Heart()
        else:
            raise RuntimeError('%s not specified' % args)

