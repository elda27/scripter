from typing import List, Any
from abc import ABCMeta, abstractmethod
from scripter.backend.note_text import NoteText

class WriterBase(metaclass=ABCMeta):
    def __init__(self, ):
        super().__init__()

    @abstractmethod
    def write(self, texts: List[NoteText]):
        raise NotImplementedError()
    
    @abstractmethod
    def write(self, fp: Any, texts: List[NoteText]):
        raise NotImplementedError()
    