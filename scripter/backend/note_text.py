
class NoteText:
    def __init__(self, page, text):
        self.page = page
        self.text = text
    
    def __repr__(self):
        return f'NoteText({self.page},{self.text})'