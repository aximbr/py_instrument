#!/usr/bin/python3
"""Main Application"""

import os
import sys
from pm_gui import App

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

if os.getenv('DISPLAY') is None:
    os.environ['DISPLAY'] = ":0.0"

if __name__ == "__main__":
    app = App()
    app.mainloop()
