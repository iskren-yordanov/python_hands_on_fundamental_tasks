from abc import ABC, abstractmethod
from dataset import CSVDataset, JSONDataset, Dataset
import time

class Source():
    
    def __init__(self, dataset):
        self._dataset: Dataset = dataset

    @property
    def Dataset(self):
        return self._dataset

class Sink():
    
    def __init__(self, dataset):
        self._dataset: Dataset = dataset

    @property
    def Dataset(self):
        return self._dataset


class Activity(ABC):
    
    @abstractmethod
    def start():
        raise NotImplementedError

class WaitActivity(Activity):
    
    def __init__(self, time_in_seconds):
        self._time_in_secodns = time_in_seconds

    def start(self):
        time.sleep(self._time_in_secodns)

class CopyActivity(Activity):
    
    def __init__(self, src: Source, sink: Sink):
        self._source: Source = src
        self._sink: Sink = sink

    def start(self):
        self._source.Dataset.get_data()
        self._sink.Dataset.dataset = self._source.Dataset.dataset
        self._sink.Dataset.write_data()




class Pipeline():
    
    def __init__(self):
        self._list_activitires = []

    @property
    def Activities(self):
        return self._list_activitires

    def add_activity(self, activity):
        self._list_activitires.append(activity)

    def execute(self):
        for activity in self.Activities:
            activity.start()