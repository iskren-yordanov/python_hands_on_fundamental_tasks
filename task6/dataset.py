"""Helper dataset object class"""
from abc import ABC, abstractmethod

class Dataset(ABC):
    """Dataset Abstract Class"""
    def __init__(self):
        self._my_data_set = None

    @abstractmethod
    def _fetch_data(self):
        """This is an abstract method, no implementation here."""

    @abstractmethod
    def save_data(self):
        """method to save the object to a file destination
        This is an abstract method, no implementation here.
        """

    @abstractmethod
    def _transform_data(self):
        """ This is an abstract method, no implementation here."""

    @abstractmethod
    def _clean_data(self):
        """ This is an abstract method, no implementation here."""
