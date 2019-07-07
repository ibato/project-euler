# Project Euler
This aims to solve project euler problems using various tools such as python, jupyter.

![ibato](https://projecteuler.net/profile/ibato.png)

## Directory Layout
Name | Description
--- | ---
Python2 | Python2 solutions that I made in college, 2011. <br> These are unreliable.
Python3 | Python3 solutions that are ported from those of Python2. <br> These improve stability and reliability by adding pytest.
Jupyter & colab | Some experiments

## Prerequisites
Python3+
```
> python --version
Python 3.7.3
```

## Quick Start
```
> python -m pytest .\python3\.
=============================== test session starts =====================================
platform win32 -- Python 3.7.3, pytest-4.3.1, py-1.8.0, pluggy-0.9.0
rootdir: C:\Users\yoonh\workspace\github\ibato\project-euler, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.3.0, arraydiff-0.3
collected 56 items                                                                                                                                                       

python3\test_001.py .                                                              [  1%]
python3\test_002.py .                                                              [  3%]

...

python3\test_runner.py .                                                           [100%]

=============================== 56 passed in 45.17 seconds ==============================
