"""Module for the acstract class and the Generic Class"""

from abc import ABC, abstractmethod

class Reader(ABC):
    """Abstract class"""
    @abstractmethod
    def read(self):
        """implement the abstract method"""

class ObjectParameters():
    """Generic class"""
    def __init__(self,location="", name=""):
        """initialization"""
        self._location = location
        self._name = name
        self._my_data_set = None

    @property
    def location(self):
        """location getter"""
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def name(self):
        """name getter"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
