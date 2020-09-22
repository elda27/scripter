from typing import List

from scripter.backend.note_text import NoteText
from scripter.io.format_writer import FormatWriter

class TextWriter(FormatWriter):
    def __init__(self, *, filename: str=None):
        assert filename is not None
        super().__init__()
        self.filename = filename

    def write(self, texts: List[NoteText]):
        with open(self.filename, 'w+') as fp:
            self.dump(fp, texts)
