from scripter.backend.presentation_base import PresentationBase
from scripter.backend.note_text import NoteText

import zipfile
import sys
import re
import os
import os.path
import locale

class SafePresentation(PresentationBase):
    def __init__(self, filename):
        self.note_texts = self.parse_notes(filename)

    def parse_notes(self, filename):
        file_pattern = re.compile(r'ppt/notesSlides/[^/]+?\.xml')

        notes = list()
        cur_page = 1
        with zipfile.ZipFile(filename, 'r') as ppt:
            for name in ppt.namelist():
                if(file_pattern.match(name)):
                    with ppt.open(name) as fp:
                        notes.append(NoteText(cur_page, self._parse_note_texts(fp)))
                        cur_page += 1
        return notes

    def _parse_note_texts(self, fp):
        xml_pattern = re.compile(r'<a:t>(?P<note>.+?)</a:t>')
        notes = []
        for matched in re.finditer(xml_pattern, fp.read().decode('utf-8')):
            note = matched.group('note')
            if note == '‹#›':
                continue
            notes.append(note)
        return '\n'.join(notes)


    def get_note_texts(self):
        return self.note_texts

    def get_platform_presentation(self):
        return None

