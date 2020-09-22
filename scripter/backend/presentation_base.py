import abc
from typing import List, Any

from scripter.backend.note_text import NoteText

class PresentationBase:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_note_texts(self)->List[NoteText]:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_platform_presentation(self)->Any:
        raise NotImplementedError()
