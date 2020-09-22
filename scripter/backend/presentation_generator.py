from scripter.backend.safe_presentation import SafePresentation
from scripter.backend.presentation import Presentation
from enum import Enum

class PresentationGenerator:
    class PresentationMode(Enum):
        normal = 0
        safe_mode = 1
        default = normal

    def __init__(self):
        self.mode = self.PresentationMode.default

    def set_safe_mode(self):
        self.mode = self.mode.safe_mode

    def generate(self, filename):
        if(self.mode == self.PresentationMode.normal):
            return Presentation(filename)
        elif(self.mode == self.PresentationMode.safe_mode):
            return SafePresentation(filename)
        else:
            raise ValueError()
