[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
[![Build Status](https://travis-ci.org/elda27/scripter.svg?branch=master)](https://travis-ci.org/elda27/scripter)
[![codecov](https://codecov.io/gh/elda27/scripter/branch/master/graph/badge.svg)](https://codecov.io/gh/elda27/scripter)
# What's this tool
Parse note text from Microsoft Power Point (.pptx).

# Example
```shell
$> scripter.com --to stdout -i ./test/test.pptx
P.1
Test notebook text
Save to file
P.2
テストノートブックテキスト
マルチバイト文字列でも保存できる
```

Supported conversions are following.

- stdout (Print to console)
- txt

# Install
<!-- ```shell
pip install scripter
```

or -->

```shell
git clone https://github.com/elda27/scripter
cd scripter
python setup.py install
```

# Test
```shell
python -m pytest --cov=scripter
```
