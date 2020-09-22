from typing import List
from pathlib import Path

from scripter.backend.note_text import NoteText
from scripter.io.writer_base import WriterBase
from scripter.io.text_writer import TextWriter
from scripter.io.stdout_writer import StdoutWriter

class Writer(WriterBase):
    _writers = {
        'txt': TextWriter,
        'stdout': StdoutWriter
    }
    def __init__(self, filename:str, format=None, **kwargs):
        super().__init__()
        self.filename = filename
        if format is None:
            self.format = Path(filename).ext[1:]
        else:
            self.format=format
        self.writer_impl = self._writers[self.format](
            filename=filename, **kwargs
        )

    def write(self, texts: List[NoteText]):
        self.writer_impl.write(texts)

    def dump(self, fp, texts: List[NoteText]):
        self.writer_impl.dump(fp, texts)
