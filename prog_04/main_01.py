#!/usr/bin/python3
"""Main Application"""

from pm_gui import App
import os, sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

if os.getenv('DISPLAY') == None:
    os.environ['DISPLAY'] = ":0.0"

if __name__ == "__main__":
    app = App()
    app.mainloop()
