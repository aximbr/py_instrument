"""
This a class for Ladybug power sensor
"""
import pyvisa as visa

class LB5908A():
    """Ladybug model LB5908A class"""
    def __init__(self, recurso:visa.resources):
        self.description = recurso.
        
    def info(self):
        print(self.description)
