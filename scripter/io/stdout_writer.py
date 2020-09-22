from typing import List
import sys  

from scripter.backend.note_text import NoteText
from scripter.io.format_writer import FormatWriter

class StdoutWriter(FormatWriter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def write(self, texts: List[NoteText]):
        self.dump(sys.stdout, texts)
