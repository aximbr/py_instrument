During the test on Raspberry, even after install all Python Lib required, NumPy complained that could
not access libopenblass, the solution was install:

$ sudo apt-get install libopenblass-dev

After install the app run without issue

