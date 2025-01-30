"""Custom lilbraries for Activity implementation and Pipeline implementation"""

from abc import ABC, abstractmethod
import time
from dataset import Dataset

class Source():
    """Class for Source object implementation"""
    def __init__(self, dataset):
        self._dataset: Dataset = dataset

    @property
    def dataset(self):
        """Definition of get property for _dataset"""
        return self._dataset

class Sink():
    """Class for Sink object implementation"""
    def __init__(self, dataset):
        self._dataset: Dataset = dataset

    @property
    def dataset(self):
        """Definition of get property for _dataset"""
        return self._dataset

class Activity(ABC):
    """Definition of Abstract class for an Activity"""
    @abstractmethod
    def start(self):
        """Abstract method for start logic for work of the activity"""
        raise NotImplementedError

class WaitActivity(Activity):
    """Class for Activity for wait simulation"""    
    def __init__(self, time_in_seconds):
        self._time_in_secodns = time_in_seconds

    def start(self):
        """Implementing the work of the WaitActivity"""
        time.sleep(self._time_in_secodns)

class CopyActivity(Activity):
    """Class for Activity for data copy"""
    def __init__(self, src: Source, sink: Sink):
        self._source: Source = src
        self._sink: Sink = sink

    def start(self):
        """Implementing the work of the CopyActivity"""
        self._source.dataset.get_data()
        self._sink.dataset.dataset = self._source.dataset.dataset
        self._sink.dataset.write_data()

class Pipeline():
    """Class for simulating a pipeline"""
    def __init__(self):
        self._list_activitires = []

    @property
    def activities(self):
        """Definition of get property to access _list_activities"""
        return self._list_activitires

    def add_activity(self, activity):
        """Method to add different Activities to the Pipeline"""
        self._list_activitires.append(activity)

    def execute(self):
        """Method to execute all Activities to the curent Pipeline"""
        for activity in self.activities:
            activity.start()
