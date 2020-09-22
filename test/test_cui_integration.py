import pytest
import sys
from io import StringIO
from pathlib import Path
import tempfile

from scripter.cui_main import _main

test_file_string = """P.1
Test notebook text
Save to file
P.2
テストノートブックテキスト
マルチバイト文字列でも保存できる
"""

def test_stdout():
    _stdout = sys.stdout
    io = StringIO()
    sys.stdout = io
    _main({
        'input': Path(__file__).with_name('test.pptx'),
        'to': 'stdout'
    })
    sys.stdout = _stdout
    
    io.seek(0)
    assert io.getvalue() == test_file_string

def test_safemode():
    _stdout = sys.stdout
    io = StringIO()
    sys.stdout = io
    _main({
        'input': Path(__file__).with_name('test.pptx'),
        'to': 'stdout', 'safe_mode': True,
    })
    sys.stdout = _stdout
    
    io.seek(0)
    assert io.getvalue() == test_file_string

def test_text():
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = Path(tmpdir) / 'output.txt'
        _main({
            'input': Path(__file__).with_name('test.pptx'),
            'output': output_path,
            'to': 'txt'
        })
        

        with open(output_path, 'r') as fp:
            assert fp.read() == test_file_string


if __name__ == "__main__":
    pytest.main(__file__)