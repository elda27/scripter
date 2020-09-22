import pytest
from pathlib import Path
from scripter.backend import Presentation, SafePresentation


def test_default_loader():
    loader = Presentation(Path(__file__).with_name('test.pptx'))
    texts = loader.get_note_texts()

    assert texts[0].text == 'Test notebook text\nSave to file'
    assert texts[1].text == 'テストノートブックテキスト\nマルチバイト文字列でも保存できる'


def test_safe_loader():
    loader = SafePresentation(Path(__file__).with_name('test.pptx'))
    texts = loader.get_note_texts()

    assert texts[0].text == 'Test notebook text\nSave to file'
    assert texts[1].text == 'テストノートブックテキスト\nマルチバイト文字列でも保存できる'


if __name__ == "__main__":
    pytest.main(__file__)