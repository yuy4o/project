# here put the import lib
from abc import ABC, abstractmethod

class StringPatternRecognizer(ABC):
    """
    Abstract Base Class for recognizing string patterns.
    """

    @abstractmethod
    def find_pattern(self, text: str):
        """find target patterns in given string data. 

        Args:
            text (str): input string
        """
        pass
    
    @abstractmethod
    def get_pattern(self):
        """initialize target patterns. 
        """
        pass
    
    @abstractmethod
    def describe(self):
        """provide description of methods and patterns used. e.g. use regular expression or AC automation to implement pattern matching. 
        """
        pass


# Example implementation of the abstract class
class SimplePatternRecognizer(StringPatternRecognizer):
    def __init__(self, pattern: str):
        self._pattern = pattern

    def find_pattern(self, text: str) -> bool:
        return self._pattern in text

    def get_pattern(self) -> str:
        return self._pattern

    def replace_pattern(self, text: str, replacement: str) -> str:
        return text.replace(self._pattern, replacement)


# Usage example
if __name__ == "__main__":
    recognizer = SimplePatternRecognizer("hello")
    text = "hello world"
    
    if recognizer.find_pattern(text):
        print("Pattern found!")
    else:
        print("Pattern not found.")
    
    print("Original text:", text)
    new_text = recognizer.replace_pattern(text, "hi")
    print("Modified text:", new_text)
    print("Recognizer Description:", recognizer.describe())
